from django.urls import path, include
from . import views
from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(f'user', viewsets.CustomUserViewSets)
router.register(f'room', viewsets.RoomViewSets)
router.register(f'rent', viewsets.RentViewSets)


urlpatterns = [
    # user endpoints
    path('', include(router.urls))
]
