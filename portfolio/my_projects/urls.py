from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'my_projects'

urlpatterns = [
    url(r'^$', views.ProjectListView.as_view(), name='projects_list'),
    url(r'^project/(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project_detail'),
    url(r'^project/new/$', views.CreateProjectView.as_view(), name='project_new'),
    url(r'^project/(?P<pk>\d+)/edit/$', views.ProjectUpdateView.as_view(), name='project_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='project_draft_list'),
    url(r'^project/(?P<pk>\d+)/remove/$', views.ProjectDeleteView.as_view(), name='project_remove'),
    url(r'^project/(?P<pk>\d+)/publish/$', views.project_publish, name='project_publish'),
]