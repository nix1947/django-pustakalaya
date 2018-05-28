from rest_framework import serializers
from pustakalaya_apps.core.models import (
    Biography,
    Keyword,
    Language,
    Publisher,
    EducationLevel,
    Sponsor,
    LicenseType,
)


# Core serializers. 
class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography 
        fields = '__all__'


class KeyWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword 
        fields = '__all__'



class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language 
        fields = '__all__'


class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel 
        fields = '__all__'



class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher 
        fields = '__all__'



class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor 
        fields = '__all__'



class LicenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseType 
        fields = '__all__'
