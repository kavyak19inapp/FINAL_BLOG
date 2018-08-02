from django.conf.urls import url
from home.views import HomeView,DetailPost,EditPost,DeletePost
from home.views import HomeView
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns=[
  url(r'^$',HomeView.as_view(),name='home'),
  url(r'^view/',views.view_post,name='view_post'),
  url(r'^(?P<pk>\d+)$',DetailPost.as_view(),name='detail'),
  url(r'^(?P<pk>\d+)/edit$',EditPost.as_view(),name='edit'),
  url(r'^(?P<pk>\d+)/delete$',DeletePost.as_view(),name='delete'),
]
