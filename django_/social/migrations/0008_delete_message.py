# Generated by Django 4.2.7 on 2023-11-10 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_alter_post_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
