# Generated by Django 3.1.7 on 2021-04-14 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockhistory',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='market',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='order_priority',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='orderday',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='ordermonth',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='orderyear',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='prod_price',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='sales',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='shipMode',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='shipday',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='shipmonth',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='shipping_cost',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='shipyear',
        ),
    ]
