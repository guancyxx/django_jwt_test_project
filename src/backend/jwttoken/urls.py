from django.urls import path

from .views.SignInView import SignInView
from .views.SignUpView import SignUpView
from .views.MeView import MeView

urlpatterns = [
    path("signin/", SignInView.as_view(), name="signin"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("me/", MeView.as_view(), name="me"),
]
