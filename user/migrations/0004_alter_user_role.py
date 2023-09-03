# Generated by Django 4.2.4 on 2023-08-30 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_is_active_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('none', 'None'), ('author', 'Author'), ('admin', 'Admin')], default='none', max_length=10),
        ),
    ]