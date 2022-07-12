from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'index.html')

def Services(request):
    return render(request, 'services.html')

def About(request):
    return render(request, 'about-us.html')

def Contact(request):
    return render(request, 'contact.html')
