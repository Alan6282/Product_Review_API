from .base import *
from app.authentication.serializers.register import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():

           user = serializer.save()
           token,_ = Token.objects.get_or_create(user=user)

           return Response({
               'user_id':user.id,
               'username':user.username,
               'token':token.key
           },status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)