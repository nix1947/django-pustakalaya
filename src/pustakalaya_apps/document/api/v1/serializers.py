from rest_framework import serializers
from pustakalaya_apps.document.models import (
    Document, 
    DocumentFileUpload,
    DocumentLinkInfo,
    DocumentSeries,
    DocumentIdentifier
) 


class DocumentLinkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentLinkInfo
        fields = '__all__'

class DocumentFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DocumentFileUpload
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    """
    Class to serialize document data types. 
    """

    documentfileupload_set = DocumentFileSerializer(many=True)
    documentlinkinfo_set = DocumentLinkInfoSerializer(many=True)
    class Meta:
        model = Document
        fields = '__all__'


class DocumentSeriesSerializer(serializers.ModelSerializer):
    """
    Class to serialize document Series data types. 
    """
    class Meta:
        model = DocumentSeries
        fields = '__all__'
    


class DocumentIdentifierSerializer(serializers.ModelSerializer):
    """
    Class to serialize DocumentIdentifier data types. 
    """
    class Meta:
        model = DocumentIdentifier
        fields = '__all__'  