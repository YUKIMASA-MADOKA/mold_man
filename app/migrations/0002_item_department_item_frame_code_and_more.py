# Generated by Django 4.2 on 2023-04-10 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='department',
            field=models.CharField(default='aaa', max_length=255, verbose_name='管理籍'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='frame_code',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='frame_height_fix_side',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='frame_height_moving_side',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='is_drawing',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='is_not_our_molds',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='manufacture_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='molding_machine',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='molds_code',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='number_of',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, verbose_name='製品名'),
        ),
    ]
