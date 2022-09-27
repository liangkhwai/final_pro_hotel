# Generated by Django 4.1.1 on 2022-09-27 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_accounts_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='customer',
            name='lastname',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
