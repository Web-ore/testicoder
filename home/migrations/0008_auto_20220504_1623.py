# Generated by Django 3.2.3 on 2022-05-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_credited_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Credited_Image',
        ),
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, default='static/Default.jpg', null=True, upload_to='static/users/'),
        ),
    ]
