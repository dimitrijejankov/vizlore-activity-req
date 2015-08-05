from django.views.generic import View
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from activity_server.models import reduced_activity_table


def reduce_activity_vector(vector):
    new_vector = [0, 0, 0, 0, 0]
    for i in xrange(len(vector)):
        new_vector[reduced_activity_table.get(i)] += vector[i]
    return new_vector


class HomeView(View):
    def get(self, request):
        return render_to_response("home.html", None, context_instance=RequestContext(request))

