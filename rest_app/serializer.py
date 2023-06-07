from .models import * 
from rest_framework import serializers

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class Carterializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"



