from rest_framework import serializers 
from pustakalaya_apps.video.models import (
    Video,
    VideoFileUpload,
    VideoLinkInfo,
    VideoSeries,
    VideoGenre
) 




class VideoSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSeries
        fields = '__all__'



class VideoGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGenre
        fields = '__all__'


class VideoLinkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLinkInfo
        fields = '__all__'

class VideoFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VideoFileUpload
        fields = '__all__'

class VideoSerializers(serializers.ModelSerializer):
    videofileupload_set = VideoFileSerializer(many=True)
    videolinkinfo_set = VideoLinkInfoSerializer(many=True)

    class Meta:
        model = Video 
        fields = '__all__'