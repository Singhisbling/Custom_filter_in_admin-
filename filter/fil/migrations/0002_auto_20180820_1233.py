# Generated by Django 2.1 on 2018-08-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bd',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='price2',
            field=models.IntegerField(default=0),
        ),
    ]