# Generated by Django 4.1.1 on 2022-09-25 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_alter_favmovie_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]