# Generated by Django 4.2.4 on 2023-09-06 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_news_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'permissions': [('can_publish_news', 'Can Publish News'), ('can_priview_news', 'Can Preview News')], 'verbose_name_plural': 'News'},
        ),
    ]