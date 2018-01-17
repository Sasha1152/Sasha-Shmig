from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'(?P<pk>\d+)/$', views.board_topics, name='board_topics')
]