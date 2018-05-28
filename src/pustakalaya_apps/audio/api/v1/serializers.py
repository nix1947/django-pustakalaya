from rest_framework import serializers
from pustakalaya_apps.audio.models import (
    Audio, 
    AudioFileUpload,
    AudioLinkInfo,  
)


class AudioLinkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioLinkInfo
        fields = '__all__'

class AudioFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AudioFileUpload
        fields = '__all__'
        


class AudioSerializers(serializers.ModelSerializer):
    audiofileupload_set = AudioFileSerializer(many=True)
    audiolinkinfo_set = AudioLinkInfoSerializer(many=True)
    class Meta:
        model = Audio
        fields = '__all__'