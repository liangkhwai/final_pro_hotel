# Generated by Django 4.1.1 on 2022-09-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0016_alter_booking_date_in_alter_booking_date_out_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(blank=True, default='ยังไม่ชำระเงิน', max_length=255),
        ),
    ]