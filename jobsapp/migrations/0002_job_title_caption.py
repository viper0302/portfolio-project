# Generated by Django 2.0.3 on 2018-03-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title_caption',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]