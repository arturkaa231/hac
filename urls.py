from django.conf.urls import url
from hac import views

urlpatterns=[
	url(r'^data/$',views.main, name='main'),]
