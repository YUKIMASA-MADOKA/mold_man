# Generated by Django 4.2 on 2023-05-12 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_temp_alter_item_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
        migrations.AlterModelOptions(
            name='temp',
            options={'verbose_name': 'アイテム', 'verbose_name_plural': 'アイテム'},
        ),
    ]
