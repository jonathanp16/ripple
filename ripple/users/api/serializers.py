from django.contrib.auth import get_user_model
from rest_framework import serializers

from ripple.users.models import User as UserType
from ripple.users.models import Reference


User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        fields = ["name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }

class ReferenceSerializer(serializers.ModelSerializer[Reference]):
    class Meta:
        model = Reference
        fields = ["user", "message"]