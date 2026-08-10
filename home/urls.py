from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='home'
urlpatterns = [
  path('home/', views.homeview, name='homeview'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)