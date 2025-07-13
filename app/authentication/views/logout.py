from .base import *
from app.authentication.serializers.logout import LogoutSerializer
from rest_framework import permissions

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def post(self,request):
     try:
        serializer = LogoutSerializer(data={},context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Message":"Successfully logged out."}, status = status.HTTP_200_OK)
     except Exception:
          return Response({"error": "Logout failed."}, status=status.HTTP_400_BAD_REQUEST)