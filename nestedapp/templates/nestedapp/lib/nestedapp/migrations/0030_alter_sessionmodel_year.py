# Generated by Django 4.1.2 on 2023-02-22 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nestedapp', '0029_semester_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionmodel',
            name='year',
            field=models.IntegerField(),
        ),
    ]
