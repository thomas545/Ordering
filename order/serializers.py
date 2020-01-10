from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import UserDetails, Order



class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        exclude = ("user",)


class OrderSerailizer(WritableNestedModelSerializer):
    user_details = UserDetailsSerializer()

    class Meta:
        model = Order
        fields = ("pizza_number", "pizza_size", "describe_order", "user_details",)

class OrderUpdateSerailizer(WritableNestedModelSerializer):

    class Meta:
        model = Order
        fields = ("pizza_number", "pizza_size", "status",)

class OrderMiniSerailizer(WritableNestedModelSerializer):
    user_details = UserDetailsSerializer()

    class Meta:
        model = Order
        fields = ("pizza_number", "pizza_size", "describe_order", "user_details",)
