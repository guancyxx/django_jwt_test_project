from rest_framework_simplejwt.views import TokenViewBase

class SignInView(TokenViewBase):
    """
    登录
    """

    _serializer_class = "jwttoken.serializers.TokenObtainPairSerializer.TokenObtainPairSerializer"