from .base import *
from app.authentication.serializers.logout import LogoutSerializer
from rest_framework import permissions

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def post(self,request):
        serializer = LogoutSerializer(data={},context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Message":"Successfully looged out."}, status = status.HTTP_200_OK)