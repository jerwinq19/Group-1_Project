from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from . import models
from . import serializers

class CustomUserViewSets(viewsets.ModelViewSet):
    
    '''
        View sets for user
    '''
    
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializers
    lookup_field = 'user_id'
    permission_classes = [AllowAny]

class RoomViewSets(viewsets.ModelViewSet):
    '''
        View sets for room
        TODO*
            make sure that only landlord can upload rooms
    '''
    
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    lookup_field = 'slug_name'
    permission_classes = [IsAuthenticated]

class RentViewSets(viewsets.ModelViewSet):
    ''''
        View sets for active rent
    '''
    queryset = models.ActiveRent.objects.all()
    serializer_class = serializers.ActiveRentSerializers
    permission_classes = [IsAuthenticated]


class RentTransactionViewSets(viewsets.ModelViewSet):
    queryset = models.RentHistory.objects.all()
    serializer_class = serializers.RentHistorySerializers
    lookup_field = 'transact_id'
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        '''
            this means that only the authenticated user can created it.
        '''
        rent = serializer.save(renter=self.request.user)
        return rent
