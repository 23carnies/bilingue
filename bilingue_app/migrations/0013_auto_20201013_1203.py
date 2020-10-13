# Generated by Django 3.1.1 on 2020-10-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilingue_app', '0012_auto_20201013_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='native_language',
            field=models.CharField(max_length=100),
        ),
    ]