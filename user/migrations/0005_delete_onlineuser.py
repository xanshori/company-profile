# Generated by Django 4.2.4 on 2023-08-30 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OnlineUser',
        ),
    ]