# Generated by Django 3.1.1 on 2020-10-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilingue_app', '0002_vocabulary'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]