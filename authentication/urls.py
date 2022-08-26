from django.urls import path
from . import views


urlpatterns = [
    path("register-member", views.RegisterMember.as_view(), name="Register User"),
    path("register-librarian", views.RegisterLibrarian.as_view(), name="register Librarian")
]