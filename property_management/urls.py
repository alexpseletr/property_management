"""
URL configuration for property_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from properties.views import PropertyListCreate, PropertyRetrieveUpdateDestroy
from adverts.views import AdvertListCreate, AdvertRetrieveUpdate
from reservations.views import ReservationListCreate, ReservationRetrieveUpdateDestroy

urlpatterns = [
    path('api/properties/', PropertyListCreate.as_view(), name='property-list-create'),
    path('api/properties/<int:id>/', PropertyRetrieveUpdateDestroy.as_view(), name='property-retrieve-update-destroy'),
    path('api/adverts/', AdvertListCreate.as_view(), name='advert-list-create'),
    path('api/adverts/<int:id>/', AdvertRetrieveUpdate.as_view(), name='advert-retrieve-update'),
    path('api/reservations/', ReservationListCreate.as_view(), name='reservation-list-create'),
    path('api/reservations/<str:reservation_id>/', ReservationRetrieveUpdateDestroy.as_view(), name='reservation-retrieve-update-destroy'),
]
