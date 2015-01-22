import json

from django.views.generic import View
from django.shortcuts import render_to_response
from django.template.context import Context, RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from activity_server.controler.data_record_controller import store_data_record

reguest_body_example = '{\
    "uuid": "2be702beae2ac34fc0d7f8ae2b5b808a402fc01a",\
    "acceleration":\
    [ \
        { "x":-0.04, "y":0, "z":9.6, "timestamp":1421933318541 },\
        { "x":-0.04, "y":0, "z":9.6, "timestamp":1421933318541 }\
    ],\
    "location":\
    [\
        { "timestamp":14219345703, "coords": {"speed": null, "heading": null, "altitude":null, "longitude":19.81996, "latitude":45.25765}},\
        { "timestamp":14219345703, "coords": {"speed": null, "heading": null, "altitude":null, "longitude":19.81996, "latitude":45.25765}}\
    ],\
    "wifi":\
        ["SrkiNetwork", "Misic Company", "Ricks", "Marko uniqe"]\
}'


class HomeView(View):
    def get(self, request):
        return render_to_response("home.html", None, context_instance=RequestContext(request))


class RESTView(View):
    def post(self, request, *args, **kwargs):
        try:
            json_object = json.loads(reguest_body_example)
            store_data_record(json_object)
        except ValueError, e:
            return HttpResponse(e.message)

        return HttpResponse('This is POST request')

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(RESTView, self).dispatch(*args, **kwargs)