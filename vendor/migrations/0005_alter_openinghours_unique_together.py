# Generated by Django 4.1.3 on 2022-12-08 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_openinghours'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='openinghours',
            unique_together={('vendor', 'day', 'from_hour', 'to_hour')},
        ),
    ]