# Generated by Django 4.2.4 on 2023-08-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plnnusantarapower', '0003_alter_intro_options_alter_intro_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]