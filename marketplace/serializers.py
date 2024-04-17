from rest_framework import serializers
from .models import Marketplace


class MarketplaceSerializer(serializers.ModelSerializer):
    """ le serializer de la Marketplace """
    user = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Marketplace
        fields = ['id', 'name', 'avatar', 'description', 'address', 'location', 'phone', 'created_time', 'updated_time', 'active', 'user']
        read_only_fields = ('created_time', 'updated_time', 'owner')

    def create(self, validated_data):
        return Marketplace.objects.create(**validated_data)