from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: blog/tag/5/
    url(r'^tag/(?P<category_id>[0-9]+)/$', views.category, name='category'),

    url(r'^write/$', views.write, name='write'),
    #url de login blog/login
    url(r'^login/$', auth_views.login, name='login'),

    url(r'^logout/$', auth_views.logout, {'next_page': '../'}, name='logout'),

]
