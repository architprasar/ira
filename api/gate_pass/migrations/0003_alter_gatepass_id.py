from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gate_pass', '0002_auto_20220811_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatepass',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
