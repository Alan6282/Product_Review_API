from .base import *
from ..serializers.review import ReviewSerializer
from ..models import Review, Product
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException


class CreateReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        user = request.user

        if Review.objects.filter(product=product, user=user).exists():
            return Response(
                {"error": "You have already reviewed this product."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(user=user, product=product)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                raise APIException("Review creation failed.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductReviewListView(APIView):
    permission_classes = [AllowAny]  

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        reviews = product.reviews.all()  
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
