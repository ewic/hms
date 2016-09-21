from django.conf.urls import url

from . import views

app_name = 'udn2'
urlpatterns = [
	# Default route
	url(r'^$', views.index, name='index'),

	# FORMS
	# New participant form
	url(r'^form/$', views.form, name='form'),

	# Participant view
	url(r'^participant/(?P<participant_id>[0-9]+)/', views.participant, name='participant'),
]

