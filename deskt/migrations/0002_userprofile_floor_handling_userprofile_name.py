# Generated by Django 5.0.1 on 2024-02-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deskt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='floor_handling',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='Anonymous', max_length=255),
        ),
    ]
