# Generated by Django 2.0.4 on 2018-04-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_userprofile_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.URLField(max_length=150, null=True),
        ),
    ]