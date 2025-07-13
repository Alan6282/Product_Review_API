from .base import *
from ..serializers.product import (
    ProductSerializer,
    ProductCreateUpdateSerializer,
)
from ..models import Product
from rest_framework.permissions import AllowAny, IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import APIException


class ProductListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Exception:
            raise APIException("Unable to fetch products.")


class ProductDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductCreateView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = ProductCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(created_by=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                raise APIException("Failed to create product.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductCreateUpdateSerializer(product, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except Exception:
                raise APIException("Product update failed.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        try:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            raise APIException("Product deletion failed.")
