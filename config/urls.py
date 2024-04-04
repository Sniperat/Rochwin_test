from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .utils import send_swagger_file


api_schema_patterns = [
    path("swagger.yaml", send_swagger_file, name="swagger_yaml"),
    path(
        "swagger",
        TemplateView.as_view(template_name="swagger-ui.html", extra_context={"schema_url": "swagger_yaml"}),
        name="swagger-ui",
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.shop.urls')),
    path('', include(api_schema_patterns)),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
