# Generated by Django 5.0.4 on 2024-04-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_contact',
            name='telephone',
            field=models.IntegerField(),
        ),
    ]
