# Generated by Django 2.2.4 on 2019-10-02 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20191001_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(upload_to='profile/'),
        ),
    ]
