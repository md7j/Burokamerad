from django.http import HttpResponse
from django.views.generic.base import TemplateView

class login(TemplateView):
    template_name = 'login.html'

class register(TemplateView):
    template_name = 'register.html'

class index(TemplateView):
    template_name = 'app.html'

class faq(TemplateView):
    template_name = 'faq.html'
