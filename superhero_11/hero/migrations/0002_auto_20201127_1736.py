# Generated by Django 3.1.1 on 2020-11-28 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='strength',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='weakness',
            field=models.CharField(max_length=255),
        ),
    ]
