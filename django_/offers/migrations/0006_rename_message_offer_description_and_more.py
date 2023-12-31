# Generated by Django 4.2.7 on 2023-11-10 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_offer_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='message',
            new_name='description',
        ),
        migrations.AddField(
            model_name='adoptrequest',
            name='message',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='offers.offer'),
            preserve_default=False,
        ),
    ]
