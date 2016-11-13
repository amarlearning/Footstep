from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^stats/$', views.stats, name="stats"),
	url(r'^stats/(?P<username>[a-z]\w+)/$', views.username, name="username")
]
