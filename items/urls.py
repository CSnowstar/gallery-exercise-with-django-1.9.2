# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from gallery_exercise import settings
from . import views


app_name = 'gallery'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^items/$', views.ItemsView.as_view(), name='item_list'),
    url(r'^items/(?P<pk>\d+)/$', views.ItemView.as_view(), name='item_detail'),
    url(r'^photos/(?P<pk>\d+)/$', views.PhotoView.as_view(), name='photo_detail'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
        ),
]
