# Generated by Django 4.2.4 on 2023-08-15 15:14

import companyprofile.validations
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0002_alter_intro_background_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='intro',
            options={'verbose_name_plural': 'Intro'},
        ),
        migrations.AlterField(
            model_name='intro',
            name='is_published',
            field=models.BooleanField(default=False, validators=[companyprofile.validations.validate_is_published_false]),
        ),
    ]
