# Generated by Django 3.1.7 on 2021-04-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0004_auto_20210415_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='issue_quantity',
            field=models.IntegerField(blank=True, default='1', null=True),
        ),
    ]
