# Generated by Django 4.1.2 on 2023-01-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nestedapp', '0017_remove_coursemodel_subject_coursemodel_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]