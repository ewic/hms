from django.conf.urls import url

from . import views

app_name = 'udn'
urlpatterns = [
	# Default route
	url(r'^$', views.index, name='index'),

	# FORMS
	# New participant form
	url(r'^form/(?P<form_type>[a-z]+)/$', views.form, name='form'),

	# Participant list
	url(r'^list/', views.list, name='list'),
	# Participant view
	url(r'^participant/(?P<participant_id>[0-9]+)/', views.participant, name='participant'),

	# Not sure if we need these...
	# Genetic Mutation view
	url(r'^gm/(?P<gm_id>[0-9]+)/$', views.gm, name='gm'),
	# Environmental Exposure view
	url(r'^ee/(?P<ee_id>[0-9]+)/$', views.ee, name='ee'),
]