# Generated by Django 4.1.2 on 2023-01-17 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nestedapp', '0019_alter_coursemodel_instructor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='creating_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
