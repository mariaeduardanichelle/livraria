# Generated by Django 5.1.3 on 2024-12-05 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_editora_cidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='passage_id',
        ),
    ]
