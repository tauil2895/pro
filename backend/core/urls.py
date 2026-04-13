from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
# Importamos las vistas oficiales de SimpleJWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('patients.urls')),
    
    # Endpoints para obtener y refrescar el token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('django_prometheus.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)