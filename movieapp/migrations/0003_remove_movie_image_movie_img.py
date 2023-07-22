# Generated by Django 4.2.3 on 2023-07-14 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='image',
        ),
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ffkff', upload_to='gallery'),
            preserve_default=False,
        ),
    ]