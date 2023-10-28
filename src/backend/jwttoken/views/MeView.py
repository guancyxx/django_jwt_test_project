__doc__="""

获取个人信息

"""

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from jwttoken.serializers.UserSerializer import UserSerializer

class MeView(RetrieveAPIView):
    """
    个人信息
    """
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

