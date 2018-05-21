from rest_framework import serializers
from pustakalaya_apps.audio.models import Audio

class AudioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'