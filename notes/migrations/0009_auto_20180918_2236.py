# Generated by Django 2.1.1 on 2018-09-18 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20180918_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalnote',
            old_name='custom_user',
            new_name='user',
        ),
    ]