# Generated by Django 3.1.5 on 2021-02-02 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='emp_ID',
            new_name='emp_nu',
        ),
    ]
