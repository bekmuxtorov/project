from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tax_officer/', include('tax_officer.urls')),
    path('karer/', include('karer.urls'))
]
