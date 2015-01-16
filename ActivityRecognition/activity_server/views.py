from django.views.generic import View
from django.shortcuts import render_to_response
from django.template.context import Context, RequestContext


class HomeView(View):

    def get(self, request):
        c = Context({"WHO": "WORLD!!!"})
        return render_to_response("home.html", None, context_instance=RequestContext(request))
