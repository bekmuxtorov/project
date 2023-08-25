from django.urls import path
from . import views


urlpatterns = [
    # Order
    path('orders/by_unique_number/<int:unique_number>/', views.orders_by_unique_number),
    path('orders/by_karer_id/<int:karer_id>/', views.orders_by_karer_id),
    path('orders/create/', views.OrderCreateAPIView.as_view()),
    path('orders/', views.OrderListAPIView.as_view()),
    path('orders/<int:pk>/', views.OrderDetailAPIView.as_view()),
    path('orders/<int:pk>/update/', views.OrderUpdateAPIView.as_view()),
    path('orders/<int:pk>/delete/', views.OrderDeleteAPIView.as_view()),
]
