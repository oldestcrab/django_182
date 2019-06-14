from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index$', views.index),
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)$', views.detail),
    url(r'^get_test1/$', views.get_test1),
    url(r'^get_test2/$', views.get_test2),
    url(r'^get_test3/$', views.get_test3),

    url(r'^post_test1/$', views.post_test1),
    url(r'^post_test2/$', views.post_test2),

    url(r'^session1/$', views.session1),
    url(r'^session2/$', views.session2),
    url(r'^session3/$', views.session3),
    url(r'^session2_handle/$', views.session2_handle),
]