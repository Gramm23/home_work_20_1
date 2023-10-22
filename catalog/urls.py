from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact')
]
