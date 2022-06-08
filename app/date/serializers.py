"""
Serializers for date APIs
"""
from rest_framework import serializers

from core.models import (
    Date,
    Todo,
)


class DateSerializer(serializers.ModelSerializer):
    """Serializer for dates."""

    class Meta:
        model = Date
        fields = ['id', 'day','description']
        read_only_fields = ['id']

#this can be failed
class DateDetailSerializer(DateSerializer):
    """Serializer for date detail view."""

    class Meta(DateSerializer.Meta):
        fields = DateSerializer.Meta.fields + ['description']

class TodoSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completion']
        read_only_fields = ['id']