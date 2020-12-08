from django.shortcuts import render
from  django.views.generic import View, TemplateView
# Create your views here.


# def storeDashboard(request):
#     return render (request, 'storeDashboard.html')

    
class StoreDashboardView(View):

    def get(self, request):
        return render(request, 'storeDashboard.html')