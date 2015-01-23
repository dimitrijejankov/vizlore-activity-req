import json

from django.views.generic import View
from django.shortcuts import render_to_response
from django.template.context import Context, RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from activity_server.controler.data_record_controller import store_data_record


class HomeView(View):
    def get(self, request):
        return render_to_response("home.html", None, context_instance=RequestContext(request))


class RESTView(View):
    def post(self, request, *args, **kwargs):

        o = json.loads(request.body)

        try:
            store_data_record(json.loads(request.body))
        except ValueError, e:
            return HttpResponse(e.message)

        response = HttpResponse('This is POST request')
        response.status_code = 200
        return response

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(RESTView, self).dispatch(*args, **kwargs)