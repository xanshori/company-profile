# Generated by Django 4.2.4 on 2023-08-27 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0021_alter_menuservices_title_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intro',
            name='background_image',
        ),
        migrations.DeleteModel(
            name='BackgroundImageIntro',
        ),
        migrations.DeleteModel(
            name='Intro',
        ),
    ]
