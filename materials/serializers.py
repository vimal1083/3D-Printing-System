
from rest_framework import serializers
from models import Materials

class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ('id', 'name')