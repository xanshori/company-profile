# Generated by Django 4.2.4 on 2023-09-04 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'permissions': [('can_publish', 'Can Publish')], 'verbose_name_plural': 'News'},
        ),
    ]
