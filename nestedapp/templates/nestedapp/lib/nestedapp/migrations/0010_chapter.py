# Generated by Django 4.1.2 on 2022-11-10 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nestedapp', '0009_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('publish', models.BooleanField(default=True)),
                ('createDate', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nestedapp.category')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nestedapp.subject')),
            ],
        ),
    ]