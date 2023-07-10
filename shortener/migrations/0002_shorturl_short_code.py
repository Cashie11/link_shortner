# Generated by Django 4.2.2 on 2023-07-09 20:54

from django.db import migrations, models
import shortener.views


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='short_code',
            field=models.CharField(default=shortener.views.generate_short_code, max_length=6, unique=True),
        ),
    ]
