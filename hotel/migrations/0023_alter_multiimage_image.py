# Generated by Django 4.1.1 on 2022-10-08 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0022_multiimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='upload/images/'),
        ),
    ]
