from rest_framework import serializers
from .models import OompaLoompa

# generic oompaloompa serializer
class OompaLoompaSerializer(serializers.ModelSerializer): 

    class Meta:
        model = OompaLoompa
        fields = '__all__'

# oompaloompa serializer for limited list (3 fields)
class OompaLoompaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OompaLoompa
        fields = ('name','age','job')