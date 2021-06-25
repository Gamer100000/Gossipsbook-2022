from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import ChatingRoom, ChatingRoomMessage, Notifications


class ChatingRoomMessageListSerializer(ModelSerializer):
    sent_by_user = serializers.StringRelatedField(read_only=True)
    to_user = serializers.SerializerMethodField()

    class Meta:
        model = ChatingRoomMessage
        exclude = ["chat_room", "user1", "user2"]

    def get_to_user(self, serializer):
        user_1 = serializer.user1
        user_2 = serializer.user2
        sent_user = serializer.sent_by_user

        if sent_user == user_1:
            return user_2.username

        return user_1.username


class NotificationSerializer(ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Notifications
        fields = "__all__"

