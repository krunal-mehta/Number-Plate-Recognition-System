# Generated by Django 3.1.3 on 2020-12-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_Main_Img',
        ),
        migrations.AddField(
            model_name='car',
            name='car_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
