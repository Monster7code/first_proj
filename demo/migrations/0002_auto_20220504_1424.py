# Generated by Django 3.1.4 on 2022-05-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Год производства'),
        ),
    ]
