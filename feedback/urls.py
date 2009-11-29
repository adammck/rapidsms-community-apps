#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from django.conf.urls.defaults import *
import views


urlpatterns = patterns('',
    url(r'^feedback$', views.index),
    url(r'^feedback/add$',         views.add,  name="add-feedback"),
    url(r'^feedback/(?P<pk>\d+)$', views.edit, name="add-feedback")
)
