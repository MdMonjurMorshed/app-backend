# Generated by Django 4.1.2 on 2023-02-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nestedapp', '0026_category_has_session_category_is_sub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='category',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='department',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='name',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='publish',
        ),
        migrations.AddField(
            model_name='semester',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='semester',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sessioncategory',
            name='semester',
            field=models.ManyToManyField(to='nestedapp.semester'),
        ),
    ]