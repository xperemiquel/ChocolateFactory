# Generated by Django 2.2.3 on 2019-07-19 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OompaLoompa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=28)),
                ('age', models.IntegerField()),
                ('job', models.CharField(max_length=28)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
    ]