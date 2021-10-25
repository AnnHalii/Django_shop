from django.views.generic import View
from django.http import HttpResponseRedirect

from .tasks import generate_csv

class GenerateCSV(View):

    def get(self, request, **kwargs):
        generate_csv.delay()
        return HttpResponseRedirect('https://www.djangoproject.com/')