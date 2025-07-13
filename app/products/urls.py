from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateDeleteView,
    CreateReviewView,
    ProductReviewListView,
)

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view()),
    path('create/', ProductCreateView.as_view()),
    path('<int:pk>/update-delete/', ProductUpdateDeleteView.as_view()),
    path('<int:pk>/review/', CreateReviewView.as_view()),
    path('<int:pk>/reviews/', ProductReviewListView.as_view()),
]