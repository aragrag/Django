# Generated by Django 4.2.5 on 2023-10-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_band_hometown'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='record_company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
