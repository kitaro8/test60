# Generated by Django 3.2.19 on 2024-03-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Magnitudew',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]