from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'whoami'

urlpatterns = [
    #url(r'^$', views.MeListView.as_view(), name='me_list'),
    url(r'^(?P<pk>\d+)$', views.MeDetailView.as_view(), name='me_detail'),
    url(r'^new/$', views.CreateMeView.as_view(), name='me_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.MeUpdateView.as_view(), name='me_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='me_draft_list'),
    url(r'^(?P<pk>\d+)/remove/$', views.MeDeleteView.as_view(), name='me_remove'),
    url(r'^(?P<pk>\d+)/publish/$', views.me_publish, name='me_publish'),
]