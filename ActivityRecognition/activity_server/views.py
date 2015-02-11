import json

from django.views.generic import View
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from activity_server.controler.store_data_record_controller import store_data_record
from activity_server.controler.fetch_data_record_controller import find_record

class HomeView(View):
    def get(self, request):
        return render_to_response("home.html", None, context_instance=RequestContext(request))


class RESTView(View):
    def post(self, request, *args, **kwargs):
        try:
            store_data_record(json.loads(request.body))
        except ValueError, e:
            response = HttpResponse("{error:%s}" % e.message)
            request.status_code = 404
            return response

        response = HttpResponse('{}')
        response.status_code = 201
        return response

    def get(self, request, *args, **kwargs):

        try:
            if 'uuid' not in request.GET:
                raise Exception("Bad request")

            record = find_record(request.GET['uuid'])

            response = HttpResponse("{date_time:'%s', "
                                    "walking:%s, sitting:%s, "
                                    "standing:%s, jogging:%s, "
                                    "biking:%s, upstairs:%s, "
                                    "downstairs:%s}" % (record.record_date,
                                                        record.walking,
                                                        record.sitting,
                                                        record.standing,
                                                        record.jogging,
                                                        record.biking,
                                                        record.upstairs,
                                                        record.downstairs))
            response.status_code = 200
            return response
        except ValueError, e:
            response = HttpResponse("{error:%s}" % e.message)
            request.status_code = 404
            return response

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(RESTView, self).dispatch(*args, **kwargs)