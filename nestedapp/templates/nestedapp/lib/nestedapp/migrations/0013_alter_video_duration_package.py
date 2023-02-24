# Generated by Django 4.1.2 on 2022-12-26 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nestedapp', '0012_rename_duratuion_video_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='duration',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nestedapp.category')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nestedapp.chapter')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nestedapp.subject')),
            ],
        ),
    ]
