# Generated by Django 4.2.4 on 2023-09-07 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LihatBerita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lihat_berita_title', models.CharField(max_length=60)),
                ('lihat_berita_description', models.TextField()),
                ('lihat_berita_button_name', models.CharField(max_length=60)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]