# Generated by Django 4.2.4 on 2023-08-31 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_rename_date_cerated_order_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for Delivery', 'Out for Delievry'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
