# Generated by Django 4.1.5 on 2023-01-20 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_customer_email_alter_customer_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
