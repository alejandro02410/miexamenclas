# Generated by Django 4.1 on 2022-10-19 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x1', models.FloatField(blank=True, null=True)),
                ('x2', models.CharField(blank=True, max_length=2, null=True)),
                ('x3', models.FloatField(blank=True, null=True)),
                ('x4', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
