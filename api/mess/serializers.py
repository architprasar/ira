from authentication.serializers import UserSerializer
from mess.models import MenuItem
from rest_framework import serializers


class MenuItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)

    class Meta:
        model = MenuItem


class MenuSlotSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=15)
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()


class WeekDaySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=15)
    slots = MenuSlotSerializer(many=True)


class MessSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=15)


class MessFeedbackSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserSerializer()
    body = serializers.CharField(max_length=500)
    mess_meal = serializers.CharField(max_length=50)
    mess_type = MessSerializer()
    created_at = serializers.DateTimeField()
    status = serializers.BooleanField(default=False)


class MessComplaintSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserSerializer()
    body = serializers.CharField(max_length=500)
    mess_meal = serializers.CharField(max_length=50)
    mess_type = MessSerializer()
    file = serializers.FileField()
    created_at = serializers.DateTimeField()
    status = serializers.BooleanField(default=False)


class MessMomSer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    file = serializers.FileField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    created_at = serializers.DateTimeField()


class MessTenderSer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    contractor = serializers.CharField(max_length=100)
    file = serializers.FileField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    archieved = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField()


class MessMenuSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    slot = MenuSlotSerializer()
    items = MenuItemSerializer(many=True)
