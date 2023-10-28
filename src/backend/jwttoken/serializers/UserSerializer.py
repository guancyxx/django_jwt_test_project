__doc__="""
个人信息获取序列化
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email")
        extra_kwargs = {"id": {"read_only": True}, "email": {"read_only": True}}

   