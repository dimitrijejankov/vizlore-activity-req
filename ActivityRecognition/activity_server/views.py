import json
import numpy as np
from django.views.generic import View
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from activity_server.controler.store_data_record_controller import store_data_record
from activity_server.controler.fetch_data_record_controller import recognize_last_activity, recognize_last_activities
from activity_server.models import activity_table_json, reduced_activity_table_json, reduced_activity_table
from activity_server.utilities.classifiers import ClassifierLoader


def reduce_activity_vector(vector):
    new_vector = [0, 0, 0, 0, 0]
    for i in xrange(len(vector)):
        new_vector[reduced_activity_table.get(i)] += vector[i]
    return new_vector


class HomeView(View):
    def get(self, request):
        return render_to_response("home.html", None, context_instance=RequestContext(request))


class RESTView(View):

    classifiers = None

    def __init__(self, **kwargs):
        super(RESTView, self).__init__(**kwargs)
        if RESTView.classifiers is None:
            RESTView.classifiers = ClassifierLoader()

    def post(self, request):
        try:
            store_data_record(json.loads(request.body), RESTView.classifiers)
        except ValueError, e:
            response = HttpResponse("{error:%s}" % e.message)
            request.status_code = 404
            return response

        response = HttpResponse('{}')
        response.status_code = 201
        return response

    def get(self, request):

        try:
            if 'uuid' not in request.GET:
                raise Exception("Bad request")

            algorithm = request.GET['alg'] if 'alg' in request.GET else 'svm'
            feature_set = request.GET['fs'] if 'fs' in request.GET else 'standard'
            current_activity = request.GET["curr_act"] if 'curr_act' in request.GET else 'false'
            ac = request.GET['ac'] if 'ac' in request.GET else '1'

            if ac != '1':
                raise Exception("Not yet implemented")

            if 'tp' in request.GET:
                record = recognize_last_activities(request.GET['uuid'],
                                                   algorithm,
                                                   feature_set,
                                                   int(request.GET['tp']))
            else:
                record = recognize_last_activity(request.GET['uuid'],
                                                 algorithm,
                                                 feature_set)

            response_text = '{ "date_time":"%s", ' % record.get("time")
            response_text += '"uuid" : "%s",' % request.GET['uuid']

            if current_activity == "true":
                response_text += '"curr_act" :  "%s",' % record.get("current_activity")
            elif current_activity != "false":
                raise Exception("Wrong value for curr_act")

            if algorithm == 'svm':
                response_text += '"svm_vector" : {'
                reduced_vec = reduce_activity_vector(record['vector'])

                for i in xrange(len(reduced_vec)):
                    if i != len(reduced_vec) - 1:
                        response_text += '"%s":"%s",' % (reduced_activity_table_json.get(i+1), reduced_vec[i])
                    else:
                        response_text += '"%s":"%s"}' % (reduced_activity_table_json.get(i+1), reduced_vec[i])

            else:
                index = np.argmax(record['vector']) + 1
                response_text += '"dt_category" : "%s"' % activity_table_json.get(index)

            response_text += "}"

            response = HttpResponse(response_text)
            response.status_code = 200
            return response
        except Exception as e:
            response = HttpResponse('{"error":"%s"}' % e.message)
            request.status_code = 404
            return response

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(RESTView, self).dispatch(*args, **kwargs)
