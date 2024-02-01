from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'
    
class ContactView(TemplateView):
    template_name = 'contact.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class ProductView(TemplateView):
    template_name = 'product.html'

class TestimonialView(TemplateView):
    template_name = 'testimonial.html'