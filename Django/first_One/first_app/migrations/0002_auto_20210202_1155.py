# Generated by Django 3.1.5 on 2021-02-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_ID',
            field=models.IntegerField(),
        ),
    ]
