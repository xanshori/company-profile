# Generated by Django 4.2.4 on 2023-09-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topbar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topbar',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
