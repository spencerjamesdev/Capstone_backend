# Generated by Django 3.2.7 on 2021-09-14 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reminders', '0002_rename_userid_reminder_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
