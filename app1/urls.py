from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('product/', ProductView.as_view(), name='product'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),


]