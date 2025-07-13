from .base import *
from app.authentication.serializers.register import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import APIException

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
          try:
           
           user = serializer.save()
           token,_ = Token.objects.get_or_create(user=user)

           return Response({
               'message': 'User registered successfully.',
               'user_id':user.id,
               'username':user.username,
               'token':token.key
           },status=status.HTTP_201_CREATED)
          
          except Exception:
                raise APIException("An unexpected error occurred during registration.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)