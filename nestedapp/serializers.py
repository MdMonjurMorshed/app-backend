from rest_framework import serializers
from .models import Package,Video,videoTopic,Category,Subject,Depertment,Chapter,Semester


class CatSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=Category
        fields="__all__"

class DepertSerializer(serializers.ModelSerializer):
    category=CatSerializer()
    class Meta:
        model=Depertment
        fields="__all__"
        
class SemesterSerializer(serializers.ModelSerializer):
    category=CatSerializer()
    department=DepertSerializer()
    class Meta:
        model=Semester
        fields="__all__"      
class SubSerializer(serializers.ModelSerializer):
    category=CatSerializer()
    class Meta:
        model=Subject
        fields="__all__"    
class ChapSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chapter
        fields="__all__"              
class PackageSerialize(serializers.ModelSerializer):
    category=CatSerializer()
    subject=SubSerializer()
    chapter=ChapSerializer()
    
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
        
        