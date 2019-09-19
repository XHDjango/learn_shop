# Generated by Django 2.2.4 on 2019-09-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'car',
            },
        ),
    ]
