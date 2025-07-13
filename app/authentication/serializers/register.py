from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):

   password = serializers.CharField(write_only=True,min_length=8)
   confirm_password = serializers.CharField(write_only=True)

   class Meta:
      model = User
      fields = ['username','password','confirm_password']
   def validate(self,data):
      if data['password'] != data['confirm_password']:
         raise ValidationError("Passwords do not match")
      return data
   def create(self,validated_data):
      validated_data.pop('confirm_password')
      user = User.objects.create_user(**validated_data)

      return user 
   