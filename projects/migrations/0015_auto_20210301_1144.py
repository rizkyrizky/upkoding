# Generated by Django 3.1.6 on 2021-03-01 11:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0014_auto_20210301_1140'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProjectEventParticipants',
            new_name='UserProjectEventParticipant',
        ),
    ]