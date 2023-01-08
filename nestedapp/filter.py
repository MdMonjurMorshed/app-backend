import django_filters
from .models import Category,Depertment,Semester,Subject,Chapter,Video
from django import forms
from taggit.forms import *


class filterModel(django_filters.FilterSet):
    parent=django_filters.ModelChoiceFilter(queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    Category_name=django_filters.CharFilter(widget=forms.TextInput(attrs={'class':'form-control'}))
    display_name=django_filters.CharFilter(widget=forms.TextInput(attrs={'class':'form-control'}))
   
    class Meta:

        model=Category
        fields={
            "Category_name":['icontains'],
            "parent":["exact"],
            "display_name":['icontains']
        }
       
class DepFilter(django_filters.FilterSet):
    category=django_filters.ModelChoiceFilter(queryset=Category.objects.all(),widget=forms.Select(attrs={"class":"form-control"}))
    depName=django_filters.CharFilter(widget=forms.TextInput(attrs={"class":"form-control"}))
    shortName=django_filters.CharFilter(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model=Depertment
        fields={
            "category":["exact"],
            "depName":["icontains"],
            "shortName":["icontains"]
        } 


class SemFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(widget=forms.TextInput(attrs={"class":"form-control"}))
    category=django_filters.ModelChoiceFilter(queryset=Category.objects.all(),widget=forms.Select(attrs={"class":"form-control"}))
    department=django_filters.ModelChoiceFilter(queryset=Depertment.objects.all(),widget=forms.Select(attrs={"class":"form-control"}))
    class Meta:
        model=Semester
        fields=['name','category','department']

# SUBJECT FILTER

class SubFilter(django_filters.FilterSet):
    name= django_filters.CharFilter(widget=forms.TextInput(attrs={'class':'form-control'}))
    category=django_filters.ModelChoiceFilter(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    subCode=django_filters.NumberFilter(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model=Subject
        fields=['name','category','subCode']        


        # FILTER FOR CHAPTER

class ChapFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(widget=forms.TextInput(attrs={'class':'form-control'}))
    subject=django_filters.ModelChoiceFilter(queryset=Subject.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model=Chapter
        fields=['name','subject']        



class TagFilter(django_filters.CharFilter):
    field_class = TagField
  

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('lookup_expr', 'in')
        super().__init__(*args, **kwargs)
            # FILTER FOR VIDEO    
class VidFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(widget=forms.TextInput(attrs={'class':'form-control'}))
    tags=TagFilter(field_name="tags__name",widget=forms.TextInput(attrs={'class':'form-control'}))
    publish=django_filters.BooleanFilter(widget=forms.Select(choices=(('',"unknown"),('True',"yes"),("False","no")),attrs={'class':'form-control'}))
    
    class Meta:
        model=Video    
        fields=['name','tags','publish']