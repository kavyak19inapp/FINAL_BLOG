from django.conf.urls import url
<<<<<<< HEAD
from home.views import HomeView,DetailPost,EditPost,DeletePost
=======
from home.views import HomeView
>>>>>>> 6c0dd6c914f92e653ee8e24941335be8686c999b
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns=[
  url(r'^$',HomeView.as_view(),name='home'),
  url(r'^view/',views.view_post,name='view_post'),
<<<<<<< HEAD
  url(r'^(?P<pk>\d+)$',DetailPost.as_view(),name='detail'),
  url(r'^(?P<pk>\d+)/edit$',EditPost.as_view(),name='edit'),

  url(r'^(?P<pk>\d+)/delete$',DeletePost.as_view(),name='delete'),

=======
>>>>>>> 6c0dd6c914f92e653ee8e24941335be8686c999b
]
