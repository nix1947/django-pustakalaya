from rest_framework import serializers 
from pustakalaya_apps.video.models import (
    Video,
    VideoFileUpload,
    VideoLinkInfo
) 


class VideoLinkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLinkInfo
        fields = '__all__'

class VideoFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VideoFileUpload
        fields = ('file_name', 'video', 'upload',)

class VideoSerializers(serializers.ModelSerializer):
    videofileupload_set = VideoFileSerializer(many=True)
    videolinkinfo_set = VideoLinkInfoSerializer(many=True)

    class Meta:
        model = Video 
        fields = '__all__'