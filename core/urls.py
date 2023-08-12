from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


def show_home(request):
    return render(request, 'index.html')


schema_view = get_schema_view(
    openapi.Info(
        title="Karer project",
        default_version="v1",
        description="Karer project API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@bekmuxtorov.me"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_home),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('api/', include('account.urls')),
    path('api/', include('tax_officer.urls')),
    path('api/', include('karer.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
