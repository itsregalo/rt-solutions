from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact

# Create your views here.

def Index(request):
    return render(request, 'index.html')

def Services(request):
    return render(request, 'services.html')

def About(request):
    return render(request, 'about-us.html')

def faq(request):
    return render(request, 'faq.html')

def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, email, message)
        db_contact = Contact(name=name, email=email, phone=phone, message=message)
        db_contact.save()
        return HttpResponseRedirect(reverse('core:contact'))

    return render(request, 'contact.html')

def why_us(request):
    return render(request, 'why-us.html')

def Handle404(request):
    return render(request, '404.html')