from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from core.views import serve_frontend

urlpatterns = [
    # Django admin
    path('django-admin/', admin.site.urls),

    # Toutes les vues backend Django (formulaires, auth, CRUD)
    path('forms/', include('core.urls')),

    # Servir les uploads (photos galerie)
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

    # Servir le frontend statique (HTML + assets)
    # Doit être en DERNIER pour ne pas intercepter les routes Django
    re_path(r'^(?P<path>.*)$', serve_frontend),
]
