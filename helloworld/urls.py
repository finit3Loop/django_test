# helloworld/urls.py
from django.conf.urls import url
from django.conf.urls.static import static
from helloworld import views
from helloworld.views import passWord

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^hasher/$', views.passWord.as_view()),
]
