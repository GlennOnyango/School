# Generated by Django 2.2.4 on 2019-08-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7)),
                ('description', models.CharField(max_length=250)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
