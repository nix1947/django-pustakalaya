from rest_framework import serializers
from pustakalaya_apps.document.models import (
    Document, DocumentFileUpload
) 

class DocumentFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DocumentFileUpload
        fields = ('file_name', 'document', 'upload',)

class DocumentSerializer(serializers.ModelSerializer):
    """
    Class to serialize document data types. 
    """

    documentfileupload_set = DocumentFileSerializer(many=True)
    class Meta:
        model = Document
        fields = '__all__'
    