# Generated by Django 3.1.7 on 2021-03-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0002_auto_20210321_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
    ]
