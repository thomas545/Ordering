from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions, exceptions, filters, status
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import OrderSerailizer, OrderUpdateSerailizer, OrderMiniSerailizer
from .models import Order, UserDetails


class OrderModelViewSet(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = OrderSerailizer
    # method_serializer_classes = {
    #     ('GET',): OrderMiniSerailizer,
    #     ('PUT',): OrderUpdateSerailizer
    # }
    queryset = Order.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ['user_details__full_name']
    ordering_fields = ['status', 'user_details__id']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrderSerailizer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = OrderSerailizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.user.pk:
            serializer.save(user=request.user)
        else:
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        serializer = OrderUpdateSerailizer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)