# Generated by Django 3.1.3 on 2020-12-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201230_0016'),
    ]

    operations = [
        migrations.CreateModel(
            name='carmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_img', models.ImageField(upload_to='car')),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]