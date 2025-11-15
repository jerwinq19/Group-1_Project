from rest_framework import serializers
from . import models


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
        # fields = '__all__'
        exclude = ['slug_name'] # this display all the fields except for the slug_name


class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Reports
        fields = '__all__'
        read_only_fields = ['report_id','room', 'reporter', 'status']

class ActiveRentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ActiveRent
        fields = '__all__'
        read_only_fields = ['rent_id'] # -> add this later if not testing using drf ['room', 'tenant']

class NotifcationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'
        read_only_fields = ['notifcation_id', 'renter', 'sender']