from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^input/$', views.JobInit.as_view()),
    url(r'^job=(?P<id>\d+)/$', views.JobView.as_view()),
    url(r'^all/$', views.JobViewList.as_view()),
]