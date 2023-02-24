from rest_framework import serializers
from .models import Package,Video,videoTopic,Category,Subject,Depertment,Chapter,Semester,CourseModel,Instructor,SessionCategory,SessionModel


class CatSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=Category
        fields="__all__"

class DepertSerializer(serializers.ModelSerializer):
    category=CatSerializer()
    class Meta:
        model=Depertment
        fields="__all__"
        
    
class SubSerializer(serializers.ModelSerializer):
    category=CatSerializer()
    class Meta:
        model=Subject
        fields="__all__"          


class VideoSerialize(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'  
      
class ChapSerializer(serializers.ModelSerializer):
    video=VideoSerialize(many=True, read_only=True)
    class Meta:
        model=Chapter
        fields=['id','name','publish','category','subject','video']
class TopicSerializer(serializers.ModelSerializer):
 
    videos=VideoSerialize()
    class Meta:
        model=videoTopic
        fields='__all__'        
        
class PackageSerialize(serializers.ModelSerializer):
    category=CatSerializer()
    subject=SubSerializer()
    chapter=ChapSerializer()
    video=TopicSerializer(many=True, read_only=True)
    class Meta:
        model=Package
        fields=['category','subject','chapter','video']          
        
class InstSerialize(serializers.ModelSerializer):
    department=DepertSerializer()
    class Meta:
        model=Instructor
        fields="__all__"      
class CourseSerialize(serializers.ModelSerializer):
    category=CatSerializer()
    department=DepertSerializer()
    subject=SubSerializer(many=True, read_only=True)
    instructor=InstSerialize()
    mentor=InstSerialize()
    
    
    class Meta:
        model= CourseModel
        fields=['id','name','category','department','subject','instructor','mentor','email','prerequisites','order','description','facebook','masenger','courseIcon','courseBanner','publish']     
        

class SemesterSerializer(serializers.ModelSerializer):
    course=CourseSerialize(many=True)
    class Meta:
        model=Semester
        fields="__all__"          
class SessionSerial(serializers.ModelSerializer) :
    class Meta:
        model=SessionModel
        fields="__all__"       
class SessionCatSerial (serializers.ModelSerializer):
    session=SessionSerial()
    category=CatSerializer()
    semester=SemesterSerializer(many=True)
  
    class Meta:
        model=SessionCategory
        fields=["session","category","semester"]     
    

       
       