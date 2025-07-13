from rest_framework import serializers
 

class LogoutSerializer(serializers.Serializer):
   def save(self,**kwargs):
     request = self.context.get('request')
     user = request.user
     user.auth_token.delete()