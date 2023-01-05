from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pardus-dists', views.get_pardus_dists),
]