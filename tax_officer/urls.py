from django.urls import path
from . import views

urlpatterns = [
    # Violation
    path('violations/create/', views.ViolationCreateAPIView.as_view()),
    path('violations/', views.ViolationListAPIView.as_view()),
    path('violations/<int:pk>/', views.ViolationDetailAPIView.as_view()),
    path('violations/<int:pk>/update/', views.ViolationUpdateAPIView.as_view()),
    path('violations/<int:pk>/delete/', views.ViolationDeleteAPIView.as_view()),
]
