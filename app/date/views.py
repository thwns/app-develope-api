"""
Views for the date APIs
"""
from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Date,
    Todo,
)
from date import serializers


class DateViewSet(viewsets.ModelViewSet):
    """View for manage date APIs."""
    serializer_class = serializers.DateDetailSerializer
    queryset = Date.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve dates for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.DateSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new date."""
        serializer.save(user=self.request.user)

class TodoViewSet(mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """Manage todos in the database."""
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-name')