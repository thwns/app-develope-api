"""
URL mappings for the date app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from date import views


router = DefaultRouter()
router.register('dates', views.DateViewSet)
router.register('todos', views.TodoViewSet)

app_name = 'date'

urlpatterns = [
    path('', include(router.urls)),
]