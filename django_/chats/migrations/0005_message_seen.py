# Generated by Django 4.2.7 on 2023-11-26 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_alter_message_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]
