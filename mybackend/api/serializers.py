from rest_framework import serializers
from api.models import Crime


class CrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crime
        fields = ['id', 'name', 'description', 'count', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
