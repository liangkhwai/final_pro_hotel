# Generated by Django 4.1.1 on 2022-09-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_alter_customer_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
