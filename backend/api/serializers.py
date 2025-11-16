from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = [
            'user_id',
            'username',
            'password',
            'email',
            'phone_number',
            'marital_status',
            'gender',
            'permanent_address',
            'budget'
        ]
        extra_kwargs = {
            "password": {"write_only":True}
        }
    
    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(**validated_data)
        return user

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'
        # exclude = ['slug_name'] # this display all the fields except for the slug_name

class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Reports
        fields = '__all__'
        read_only_fields = ['report_id','room', 'reporter', 'status']

class ActiveRentSerializers(serializers.ModelSerializer):
    room_name = serializers.SerializerMethodField()
    tenant_name = serializers.SerializerMethodField()
    
    class Meta:
        model = models.ActiveRent
        fields = '__all__'
        read_only_fields = ['rent_id', 'room', 'tenant', 'start_date', 'due_date', 'rent_transaction', 'status', 'amount'] # -> add this later if not testing using drf ['room', 'tenant']

    def get_room_name(self, obj):
        return obj.room.name

    def get_tenant_name(self, obj):
        return obj.tenant.username

class NotifcationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'
        read_only_fields = ['notifcation_id', 'renter', 'sender']

class RentHistorySerializers(serializers.ModelSerializer):
    room_name = serializers.SerializerMethodField()
    class Meta:
        model = models.RentHistory
        fields = ['id', 'transact_id', 'room','room_name']
        read_only_fields = ['id', 'renter']

    def get_room_name(self, obj):
        return f"{obj.room.name}"
    
    def validate(self, attrs):
        '''
            TODAYS LEARNING..
            you cannot access a key if its in the read only fields
        '''
        renter_budget = self.context['request'].user
        room_price = attrs['room'].price
                
        if renter_budget.budget < room_price:
            raise serializers.ValidationError({
                "budget": "You budget is lower than the room price.."
            })
        return attrs