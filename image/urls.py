from django.conf.urls import *
from image.views import *

urlpatterns = patterns('',
    url(r'^init/$',init),
    url(r'^upload/$',upload),
)