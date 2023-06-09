# Generated by Django 4.2 on 2023-05-12 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_molds_code_item_mold_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fa', models.CharField(blank=True, max_length=255, null=True, verbose_name='A')),
                ('fb', models.CharField(blank=True, max_length=255, null=True, verbose_name='B')),
                ('fc', models.CharField(blank=True, max_length=255, null=True, verbose_name='C')),
                ('fd', models.CharField(blank=True, max_length=255, null=True, verbose_name='D')),
                ('fe', models.CharField(blank=True, max_length=255, null=True, verbose_name='E')),
                ('ff', models.CharField(blank=True, max_length=255, null=True, verbose_name='F')),
                ('fg', models.CharField(blank=True, max_length=255, null=True, verbose_name='G')),
                ('fh', models.CharField(blank=True, max_length=255, null=True, verbose_name='H')),
                ('fi', models.CharField(blank=True, max_length=255, null=True, verbose_name='I')),
                ('fj', models.CharField(blank=True, max_length=255, null=True, verbose_name='J')),
                ('fk', models.CharField(blank=True, max_length=255, null=True, verbose_name='K')),
                ('fl', models.CharField(blank=True, max_length=255, null=True, verbose_name='L')),
                ('fm', models.CharField(blank=True, max_length=255, null=True, verbose_name='M')),
                ('fn', models.CharField(blank=True, max_length=255, null=True, verbose_name='N')),
                ('fo', models.CharField(blank=True, max_length=255, null=True, verbose_name='O')),
                ('fp', models.CharField(blank=True, max_length=255, null=True, verbose_name='P')),
                ('fq', models.CharField(blank=True, max_length=255, null=True, verbose_name='Q')),
                ('fr', models.CharField(blank=True, max_length=255, null=True, verbose_name='R')),
                ('fs', models.CharField(blank=True, max_length=255, null=True, verbose_name='S')),
                ('ft', models.CharField(blank=True, max_length=255, null=True, verbose_name='T')),
                ('fu', models.CharField(blank=True, max_length=255, null=True, verbose_name='U')),
                ('fv', models.CharField(blank=True, max_length=255, null=True, verbose_name='V')),
                ('fw', models.CharField(blank=True, max_length=255, null=True, verbose_name='W')),
                ('fx', models.CharField(blank=True, max_length=255, null=True, verbose_name='X')),
                ('fy', models.CharField(blank=True, max_length=255, null=True, verbose_name='Y')),
                ('fz', models.CharField(blank=True, max_length=255, null=True, verbose_name='Z')),
                ('faa', models.CharField(blank=True, max_length=255, null=True, verbose_name='AA')),
                ('fab', models.CharField(blank=True, max_length=255, null=True, verbose_name='AB')),
                ('fac', models.CharField(blank=True, max_length=255, null=True, verbose_name='AC')),
                ('fad', models.CharField(blank=True, max_length=255, null=True, verbose_name='AD')),
                ('fae', models.CharField(blank=True, max_length=255, null=True, verbose_name='AE')),
                ('faf', models.CharField(blank=True, max_length=255, null=True, verbose_name='AF')),
                ('fag', models.CharField(blank=True, max_length=255, null=True, verbose_name='AG')),
                ('fah', models.CharField(blank=True, max_length=255, null=True, verbose_name='AH')),
                ('fai', models.CharField(blank=True, max_length=255, null=True, verbose_name='AI')),
                ('faj', models.CharField(blank=True, max_length=255, null=True, verbose_name='AJ')),
                ('fak', models.CharField(blank=True, max_length=255, null=True, verbose_name='AK')),
                ('fal', models.CharField(blank=True, max_length=255, null=True, verbose_name='AL')),
                ('fam', models.CharField(blank=True, max_length=255, null=True, verbose_name='AM')),
                ('fan', models.CharField(blank=True, max_length=255, null=True, verbose_name='AN')),
                ('fao', models.CharField(blank=True, max_length=255, null=True, verbose_name='AO')),
                ('fap', models.CharField(blank=True, max_length=255, null=True, verbose_name='AP')),
                ('faq', models.CharField(blank=True, max_length=255, null=True, verbose_name='AQ')),
                ('far', models.CharField(blank=True, max_length=255, null=True, verbose_name='AR')),
                ('fas', models.CharField(blank=True, max_length=255, null=True, verbose_name='AS')),
                ('fat', models.CharField(blank=True, max_length=255, null=True, verbose_name='AT')),
                ('fau', models.CharField(blank=True, max_length=255, null=True, verbose_name='AU')),
                ('fav', models.CharField(blank=True, max_length=255, null=True, verbose_name='AV')),
                ('faw', models.CharField(blank=True, max_length=255, null=True, verbose_name='AW')),
                ('fax', models.CharField(blank=True, max_length=255, null=True, verbose_name='AX')),
                ('fay', models.CharField(blank=True, max_length=255, null=True, verbose_name='AY')),
                ('faz', models.CharField(blank=True, max_length=255, null=True, verbose_name='AZ')),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='製品名'),
        ),
    ]
