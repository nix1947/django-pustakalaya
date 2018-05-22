from rest_framework import serializers
from pustakalaya_apps.document.models import (
    Document, 
    DocumentFileUpload,
    DocumentLinkInfo
) 


class DocumentLinkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentLinkInfo
        fields = '__all__'

class DocumentFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DocumentFileUpload
        fields = ('file_name', 'document', 'upload',)

class DocumentSerializer(serializers.ModelSerializer):
    """
    Class to serialize document data types. 
    """

    documentfileupload_set = DocumentFileSerializer(many=True)
    documentlinkinfo_set = DocumentLinkInfoSerializer(many=True)
    class Meta:
        model = Document
        fields = '__all__'
    