from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',HomeView,name='home'),
    path('login/',LoginView,name='login'),
    path('logout/',LogoutView,name='logout'),
    path('register/',RegisterView,name='register')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)