# Generated by Django 3.1.1 on 2020-10-14 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bilingue_app', '0002_auto_20201014_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='chiste',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bilingue_app.customuser'),
            preserve_default=False,
        ),
    ]