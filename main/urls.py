from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views


 
urlpatterns = [
     path('', views.home, name='home'),
    
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)