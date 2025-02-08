from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('idempotence-authenticator', views.idempotenceAuthenticator, name='Idempotence Authenticator'),
]
