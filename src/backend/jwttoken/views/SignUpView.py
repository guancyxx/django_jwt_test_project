__doc__="""
This file contains the SignUpView class, which is used to create a new user.

The SignUpView class is a subclass of the CreateAPIView class, which is a generic view that provides a post method handler.
"""

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from jwttoken.serializers.SignUpSerializer import SignUpSerializer
from jwttoken.utils import ip_filter
from django.utils.decorators import method_decorator

@method_decorator(ip_filter, name="dispatch")
class SignUpView(CreateAPIView):
    """
    注册
    """
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)