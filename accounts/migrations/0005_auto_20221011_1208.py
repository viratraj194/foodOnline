# Generated by Django 3.1.5 on 2022-10-11 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20221011_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='address_line_1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address_line_2',
        ),
    ]
