from django.views.generic import View
from django.shortcuts import render_to_response
from django.template.context import RequestContext


class HomeView(View):
    def get(self, request):
        return render_to_response("home.html", None, context_instance=RequestContext(request))
