# Generated by Django 4.1.2 on 2022-11-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nestedapp', '0004_alter_category_category_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depertment',
            name='depIcon',
            field=models.ImageField(blank=True, upload_to='DepIcon/'),
        ),
        migrations.AlterField(
            model_name='depertment',
            name='depThumbnail',
            field=models.ImageField(blank=True, upload_to='DepThumbnail/'),
        ),
    ]