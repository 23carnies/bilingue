# Generated by Django 3.1.1 on 2020-10-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilingue_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
