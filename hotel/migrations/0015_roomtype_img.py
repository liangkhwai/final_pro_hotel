# Generated by Django 4.1.1 on 2022-09-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0014_alter_customer_account_delete_accounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='upload/images/'),
        ),
    ]
