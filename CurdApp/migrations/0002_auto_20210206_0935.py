# Generated by Django 3.1.6 on 2021-02-06 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CurdApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
