# Generated by Django 4.0.4 on 2022-06-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0003_remove_menuitem_slot_remove_menuitem_week_day_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('week_days', models.ManyToManyField(to='mess.weekday')),
            ],
        ),
    ]
