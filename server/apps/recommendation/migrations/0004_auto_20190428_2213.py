# Generated by Django 2.1.4 on 2019-04-28 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0003_auto_20190428_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='random_rank',
            field=models.FloatField(default=0, max_length=255, verbose_name='随机排序因子'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='doubanId',
            field=models.CharField(max_length=20, verbose_name='豆瓣id'),
        ),
    ]