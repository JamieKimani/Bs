from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'customer/about.html')
def contact(request):
    return render(request, 'customer/contact.html')
def home(request):
    return render(request, 'customer/home.html')
def profile(request):
    return render(request, 'customer/profile.html')

