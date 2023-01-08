import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","nested.settings")
import django
django.setup()
import random
from nestedapp.models import Video
from faker import Faker
fake=Faker()

def populate(value):
    for i in range(value):
        
        name=fake.name()
      
        url=fake.url()
       
   
        obj=Video.objects.get_or_create(name=name,url=url)
    
def main():
    no=int(input("enter the number you want:"))
    populate(no)
if __name__=="__main__":
    main()       