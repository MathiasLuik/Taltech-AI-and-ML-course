# Generated by Django 2.1.3 on 2018-11-18 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20181118_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
