# Generated by Django 3.1.3 on 2020-11-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admindb',
            name='lexpiredate',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='admindb',
            name='lissuedate',
            field=models.CharField(max_length=50),
        ),
    ]