from urllib import request

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'customer/index.html')
def portfolio(request):
    return render(request, 'customer/portfolio-details.html')
def service_details(request):
    return render(request, 'customer/service-details.html')
def starter_page(request):
    return render(request, 'customer/starter-page.html')
