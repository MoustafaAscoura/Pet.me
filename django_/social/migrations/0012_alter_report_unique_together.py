# Generated by Django 4.2.7 on 2023-11-19 07:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0011_alter_comment_options_alter_reply_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='report',
            unique_together={('user', 'post', 'comment')},
        ),
    ]
