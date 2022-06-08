"""
Serializers for date APIs
"""
from rest_framework import serializers

from core.models import (
    Date,
    Todo,
)

class TodoSerializer(serializers.ModelSerializer):
    """Serializer for todos."""

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completion']
        read_only_fields = ['id']


class DateSerializer(serializers.ModelSerializer):
    """Serializer for dates."""
    todos = TodoSerializer(many=True, required=False)

    class Meta:
        model = Date
        fields = ['id', 'day', 'description', 'todos']
        read_only_fields = ['id']

    def _get_or_create_todos(self, todos, date):
        """Handle getting or creating todos as needed."""
        auth_user = self.context['request'].user
        for todo in todos:
            todo_obj, created = Todo.objects.get_or_create(
                user=auth_user,
                **todo,
            )
            date.tags.add(todo_obj)

    def create(self, validated_data):
        """Create a recipe."""
        tags = validated_data.pop('tags', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)

        return date

    def update(self, instance, validated_data):
        """Update recipe."""
        tags = validated_data.pop('tags', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

#this can be failed
class DateDetailSerializer(DateSerializer):
    """Serializer for date detail view."""

    class Meta(DateSerializer.Meta):
        fields = DateSerializer.Meta.fields + ['description']
