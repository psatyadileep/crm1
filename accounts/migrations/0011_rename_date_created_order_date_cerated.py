# Generated by Django 4.2.4 on 2023-08-31 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_rename_date_cerated_order_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_created',
            new_name='date_cerated',
        ),
    ]
