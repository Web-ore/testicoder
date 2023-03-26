# Generated by Django 3.2.3 on 2022-04-30 12:28

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='User_profile',
            field=models.ImageField(blank=True, default='static/Default.jpg', null=True, upload_to='static/users/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
