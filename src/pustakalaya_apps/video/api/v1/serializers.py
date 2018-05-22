from rest_framework import serializers 
from pustakalaya_apps.video.models import Video 


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video 
        fields = '__all__'