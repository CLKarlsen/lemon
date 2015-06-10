from django.conf.urls import patterns, url
from useraccounts import views

urlpatterns = patterns('',
	url(r'^register$', views.user_register, name='user_register'),
	url(r'^edit_profile$', views.user_edit_profile, name='user_edit_profile'),
	url(r'^login$', views.user_login, name='user_login'),
	url(r'^logout$', views.user_logout, name='user_logout'),
	url(r'^user_profile$', views.user_profile, name='user_profile'),
	)