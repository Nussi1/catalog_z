# Generated by Django 4.0.4 on 2022-05-12 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='choice',
            field=models.CharField(blank=True, choices=[('Python', 'Python'), ('Java', 'Java')], max_length=255),
        ),
    ]
