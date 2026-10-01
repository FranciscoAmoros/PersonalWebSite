from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("post/<slug:slug>/comentar/", views.add_comment, name="add_comment"),
    path("registro/", views.register, name="register"),
]