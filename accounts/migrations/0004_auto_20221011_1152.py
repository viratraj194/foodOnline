# Generated by Django 3.1.5 on 2022-10-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220910_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='longitude',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
