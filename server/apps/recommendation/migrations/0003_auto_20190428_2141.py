# Generated by Django 2.1.4 on 2019-04-28 21:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recommendation', '0002_auto_20190428_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='doubanId',
            field=models.CharField(default='', max_length=20, verbose_name='豆瓣id'),
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='doubanIds',
        ),
        migrations.AlterUniqueTogether(
            name='recommendation',
            unique_together={('user', 'doubanId')},
        ),
    ]
