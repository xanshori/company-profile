# Generated by Django 4.2.4 on 2023-08-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options_alter_news_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(default='', max_length=55),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=100),
        ),
    ]