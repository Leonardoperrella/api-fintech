# Generated by Django 2.2.1 on 2019-05-05 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_auto_20190505_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='loan_id',
            new_name='loan',
        ),
    ]
