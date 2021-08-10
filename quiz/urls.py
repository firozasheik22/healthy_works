from django.conf.urls import url
from django.urls import path
from django.http import HttpResponse
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('<int:courseid>/',views.detail,name='detail'),
    path('',views.quiz,name='quiz')
]