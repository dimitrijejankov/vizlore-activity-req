import json
import numpy as np
from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from activity_server.controler.hidden_store_data_record_controller import store_data_record
from activity_server.controler.hidden_fetch_data_record_controller import recognize_last_activities
from activity_server.controler.hidden_fetch_data_record_controller import recognize_last_activity
from activity_server.models import reduce_activity_vector, activity_table_json
from activity_server.utilities.classifiers import ClassifierLoader


class RestView(View):

    classifiers = None

    def __init__(self, **kwargs):
        super(RestView, self).__init__(**kwargs)
        if RestView.classifiers is None:
            RestView.classifiers = ClassifierLoader()

    def post(self, request):
        try:
            store_data_record(json.loads(request.body), RestView.classifiers)
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

            uuid = request.GET['uuid']
            alg = request.GET['alg'] if 'alg' in request.GET else 'svm'
            fs = request.GET['fs'] if 'fs' in request.GET else 'standard'
            curr_act = request.GET["curr_act"] if 'curr_act' in request.GET else 'false'
            ac = request.GET['ac'] if 'ac' in request.GET else '1'
            start_ts = int(request.GET['start_ts']) if 'start_ts' in request.GET else None
            end_ts = int(request.GET['end_ts']) if 'end_ts' in request.GET else None

            if ac != '1':
                raise Exception("Context not yet implemented!")

            if start_ts is not None and end_ts is not None:
                record = recognize_last_activities(uuid, alg, fs, start_ts, end_ts)
            else:
                record = recognize_last_activity(uuid, alg, fs)

            response = {"date_time": unicode(record.get("time")), "uuid": uuid}

            if curr_act == "true":
                response["curr_act"] = record.get("curr_act")
            elif curr_act != "false":
                raise Exception("Wrong value for curr_act")

            if alg == 'svm':
                response['svm_vector'] = reduce_activity_vector(record['vector'])
            else:
                response['dt_category'] = activity_table_json.get(np.argmax(record['vector']) + 1)

            response = HttpResponse(json.dumps(response))
            response.status_code = 200
            return response
        except Exception as e:
            response = HttpResponse('{"error":"%s"}' % e.message)
            request.status_code = 404
            return response

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(RestView, self).dispatch(*args, **kwargs)
