# Generated by Django 2.1.4 on 2019-04-26 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0007_auto_20190426_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorgenre',
            name='genre',
            field=models.CharField(max_length=100, verbose_name='种类'),
        ),
    ]
