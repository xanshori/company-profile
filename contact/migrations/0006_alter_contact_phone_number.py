# Generated by Django 4.2.4 on 2023-09-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
