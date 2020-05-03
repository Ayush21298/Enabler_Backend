from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^udemy/$', views.udemy, name='udemy'),
	url(r'^coursera/$', views.coursera, name='coursera'),
	url(r'^edx/$', views.edx, name='edx'),
]