from django.urls import path
from . import views


urlpatterns = [
    # Karers
    path('karers/create/', views.KarerCreateAPIView.as_view()),
    path('karers/', views.KarerListAPIView.as_view()),
    path('karers/<int:pk>/', views.KarerDetailAPIView.as_view()),
    path('karers/<int:pk>/update/', views.KarerUpdateAPIView.as_view()),
    path('karers/<int:pk>/delete/', views.KarerDeleteAPIView.as_view()),

    # Order
    path('orders/create/', views.OrderCreateAPIView.as_view()),
    path('orders/', views.OrderListAPIView.as_view()),
    path('orders/<int:pk>/', views.OrderDetailAPIView.as_view()),
    path('orders/<int:pk>/update/', views.OrderUpdateAPIView.as_view()),
    path('orders/<int:pk>/delete/', views.OrderDeleteAPIView.as_view()),
]
