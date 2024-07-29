# myapp/urls.py

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Route for the list of items
    path('', views.item_list, name='item_list'),

    # Route for item detail view
    path('item/<int:id>/', views.item_detail, name='item_detail'),
]

# Include these only in development; in production, use a web server for static/media files
if settings.DEBUG:  # Only serve static and media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
