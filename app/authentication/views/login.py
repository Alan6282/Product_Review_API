from .base import *
from app.authentication.serializers.login import LoginSerializer
from rest_framework.authtoken.models  import Token
from rest_framework.permissions import AllowAny


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user =  serializer.validated_data['user']
            token,_ = Token.objects.get_or_create(user=user)
            return Response({'user_id':user.id,
                             'username':user.username,
                             'token':token.key
                             },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
