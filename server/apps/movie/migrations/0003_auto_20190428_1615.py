# Generated by Django 2.1.4 on 2019-04-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_genre_doubanids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
        migrations.AddField(
            model_name='movie',
            name='movidId',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='数据集id'),
        ),
    ]
