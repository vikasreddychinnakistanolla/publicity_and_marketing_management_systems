# Generated by Django 3.2.2 on 2021-05-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200414_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(default=800),
            preserve_default=False,
        ),
    ]
