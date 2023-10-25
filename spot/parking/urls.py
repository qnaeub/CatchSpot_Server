from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# DRF 라우터
router = DefaultRouter()
router.register(r'reservationInfo', views.ReservationInfoViewSet, basename='reservationInfo')
router.register(r'parkingLot', views.ParkingLotViewSet, basename='parkingLot')
router.register(r'parkingZone', views.ParkingZoneViewSet, basename='parkingZone')
router.register(r'reservationState', views.ReservationStateViewSet, basename='reservationState')
router.register(r'parkingState', views.ParkingStateViewSet, basename='parkingState')

# URL 지정
urlpatterns = [
    path('getParkingLotList/', views.get_parkingLot_list),
    path('getParkableZone/', views.get_parkableZone_list),
    path('', include(router.urls)),
]