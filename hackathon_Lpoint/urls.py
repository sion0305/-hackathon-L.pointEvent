from django.contrib import admin
from django.urls import path, include
import mainapp.views
import eventapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
 
    path('', include('mainapp.urls')),
    path('', include('eventapp.urls')),  
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
