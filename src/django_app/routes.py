# django_app/routes.py

from django.urls import include, path

urlpatterns = [
  path('places/', include('modules.places.urls')),
]