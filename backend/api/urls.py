from django.urls import path, include
from . import views
from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(f'user', viewsets.CustomUserViewSets)
router.register(f'room', viewsets.RoomViewSets)
router.register(f'rent', viewsets.RentViewSets)
router.register(f'history', viewsets.RentHistoryViewSets)


urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name="logout_view"),
    
    # user endpoints
    path('', include(router.urls))
]
