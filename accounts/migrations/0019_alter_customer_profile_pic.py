# Generated by Django 4.2.4 on 2023-09-15 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_customer_profile_pic_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile.img', null=True, upload_to='media/'),
        ),
    ]