from diet_diary.models import Product, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        view_name='product-detail',
        read_only=True,
        many=True,
    )

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.HyperlinkedRelatedField(
        view_name='category-detail',
        read_only=True,
    )

    class Meta:
        model = Product
        fields = '__all__'