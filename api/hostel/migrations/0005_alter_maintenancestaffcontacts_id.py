# Generated by Django 4.1 on 2022-08-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0004_auto_20220811_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancestaffcontacts',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
