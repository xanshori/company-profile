# Generated by Django 4.2.4 on 2023-09-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_news_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=models.ImageField(blank=True, default='static/assets/img/defaultnewskotak.png', null=True, upload_to='media/news'),
        ),
    ]
