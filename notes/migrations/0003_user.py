# Generated by Django 2.1.1 on 2018-09-17 22:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20180917_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
