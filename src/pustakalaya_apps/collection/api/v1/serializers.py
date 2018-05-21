from rest_framework import serializers
from pustakalaya_apps.collection.models import Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection 
        fields = '__all__'

        