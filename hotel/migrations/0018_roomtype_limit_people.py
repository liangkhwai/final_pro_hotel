# Generated by Django 4.1.1 on 2022-10-05 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0017_alter_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='limit_people',
            field=models.IntegerField(default=0),
        ),
    ]