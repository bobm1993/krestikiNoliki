from django.conf.urls import url

from krestikiNolikiApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^game', views.game, name='game'),
    url(r'^history', views.history, name='history')
]
