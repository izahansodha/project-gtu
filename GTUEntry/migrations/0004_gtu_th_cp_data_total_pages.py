# Generated by Django 5.1.7 on 2025-04-07 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GTUEntry', '0003_gtu_th_cp_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='gtu_th_cp_data',
            name='total_pages',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
