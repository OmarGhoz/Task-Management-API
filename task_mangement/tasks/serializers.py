from rest_framework import serializers
from .models import Task, CustomUser
from django.contrib.auth.hashers import make_password
from django.utils.timezone import now


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser.objects.create_user(**validated_data)
        return user


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "due_date", "priority", "status", "completed_at", "user"]
        read_only_fields = ["completed_at", "user"]

    def validate_due_date(self, value):
        if value <= now():
            raise serializers.ValidationError("Due date must be in the future.")
        return value


    def validate_priority(self, value):
        if value not in [p[0] for p in Task.PRIORITY_CHOICES]:
            raise serializers.ValidationError("Invalid priority value.")
        return value

    def validate_status(self, value):
        if value not in [s[0] for s in Task.STATUS_CHOICES]:
            raise serializers.ValidationError("Invalid status value.")
        return value