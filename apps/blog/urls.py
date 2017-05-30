from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: blog/tag/5/
    url(r'^tag/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),

    url(r'^write/$', views.FormCreate.as_view(), name='write'),
    #url de login blog/login
    url(r'^login/$', auth_views.login, name='login'),

    url(r'^logout/$', auth_views.logout, {'next_page': '../'}, name='logout'),

]
