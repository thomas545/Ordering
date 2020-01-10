from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'order', views.OrderModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('myorder/<int:pk>/', views.OrderView.as_view()),
]
