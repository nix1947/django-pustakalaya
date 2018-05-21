from rest_framework import serializers
from pustakalaya_apps.document.models import Document 

class DocumentSerializer(serializers.ModelSerializer):
    """
    Class to serialize document data types. 
    """

    class Meta:
        model = Document
        fields = '__all__'
       