# Generated by Django 4.2.4 on 2023-09-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=models.ImageField(blank=True, default='static/assets/img/news_plnnp.jpg', null=True, upload_to='media/news'),
        ),
    ]