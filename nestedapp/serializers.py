from rest_framework import serializers
from .models import Package,Video,videoTopic


class PackageSerialize(serializers.ModelSerializer):
    class Meta:
        model=Package
        fields='__all__'

class VideoSerialize(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'  

class TopicSerializer(serializers.ModelSerializer):
    name=PackageSerialize()
    videos=VideoSerialize()
    class Meta:
        model=videoTopic
        fields='__all__'        