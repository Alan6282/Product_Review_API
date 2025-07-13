from .base import *
from app.authentication.serializers.login import LoginSerializer
from rest_framework.authtoken.models  import Token
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import APIException


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
     try:
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user =  serializer.validated_data['user']
            token,_ = Token.objects.get_or_create(user=user)
            return Response({'user_id':user.id,
                             'username':user.username,
                             'token':token.key
                             },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     except Exception as e:
        raise APIException("Something went wrong during login.")
