from django.urls import path
from . import views

urlpatterns = [
    # Profile
    path('profiles/create/', views.ProfileCreateAPIView.as_view()),
    path('profiles/', views.ProfileListAPIView.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetailAPIView.as_view()),
    path('profiles/<int:pk>/update/', views.ProfileUpdateAPIView.as_view()),
    path('profiles/<int:pk>/delete/', views.ProfileDeleteAPIView.as_view()),

    # Violation
    path('violations/create/', views.ViolationCreateAPIView.as_view()),
    path('violations/', views.ViolationListAPIView.as_view()),
    path('violations/<int:pk>/', views.ViolationDetailAPIView.as_view()),
    path('violations/<int:pk>/update/', views.ViolationUpdateAPIView.as_view()),
    path('violations/<int:pk>/delete/', views.ViolationDeleteAPIView.as_view()),
]
