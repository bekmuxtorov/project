from django.urls import path

from . import views

urlpatterns = [
    # Verify code
    path('sent_code/', views.sent_verification_code),
    path('verify_code/', views.verify_code),

    # Login
    path('auth/login/', views.UserLoginApiView.as_view(), name='login_view'),

    # Tax officer
    path('auth/register/tax_officer/', views.TaxOfficerRegisterAPIView.as_view()),

    # Karer
    path('auth/register/karer/', views.KarerRegisterAPIView.as_view()),
    path('karer/<int:pk>/', views.KarerDetailAPIView.as_view()),
    path('karer/by_name/', views.KarerListAPIView.as_view()),

    # Region
    path('regions/create/', views.RegionCreateAPIView.as_view()),
    path('regions/', views.RegionListAPIView.as_view()),
    path('regions/<int:pk>/', views.RegionDetailAPIView.as_view()),
    path('regions/<int:pk>/update/', views.RegionUpdateAPIView.as_view()),
    path('regions/<int:pk>/delete/', views.RegionDeleteAPIView.as_view()),

]
