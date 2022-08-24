from unicodedata import name
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', views.home, name='home'),
  path('about/',views.about,name='about'),
  path('departments/',views.departments,name='departments'),
  path('gallery/',views.gallery, name='gallery'),
  path('contact/',views.contact, name='contact'),
]






if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)