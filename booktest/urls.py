from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index$', views.index),
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)$', views.detail),
]