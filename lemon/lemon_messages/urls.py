from django.conf.urls import patterns, url

from lemon_messages import views

urlpatterns = patterns('',
	url(r'^$', views.message_wall, name='message_wall'),
	url(r'^(\d+)/$', views.message_details, name='message_details'),
	url(r'^(\d+)/add_likes$', views.add_likes, name='add_likes'),
)