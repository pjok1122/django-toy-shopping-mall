# Generated by Django 2.2.4 on 2019-08-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='reg_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='등록시간'),
        ),
    ]
