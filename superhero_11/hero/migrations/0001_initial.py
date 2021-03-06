# Generated by Django 3.1.3 on 2020-11-20 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('identity', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('strength', models.CharField(max_length=20)),
                ('weakness', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
