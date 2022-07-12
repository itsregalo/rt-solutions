from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', Index, name='index'),
    path('services/', Services, name='services'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('why-us/', why_us, name='why-us'),
]
