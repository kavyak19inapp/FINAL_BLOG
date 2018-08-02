from django.conf.urls import url
from home.views import HomeView
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns=[
  url(r'^$',HomeView.as_view(),name='home'),
  url(r'^view/',views.view_post,name='view_post'),
]
