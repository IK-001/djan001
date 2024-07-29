# myemart/urls.py

from django.contrib import admin
from django.urls import path, include
from myapp import views  # Import views from myapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.item_list, name='home'),  # Direct root URL to item_list view
    path('myapp/', include('myapp.urls')),  # Include URLs from the myapp application
]

# Serve static and media files in development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
