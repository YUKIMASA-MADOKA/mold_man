# Generated by Django 4.2 on 2023-05-12 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_temp_options_remove_item_age_remove_item_sex_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
