from django.urls import path

from . import views

urlpatterns = [
    path("munchapp/", views.munchapp, name="munchapp"),
]