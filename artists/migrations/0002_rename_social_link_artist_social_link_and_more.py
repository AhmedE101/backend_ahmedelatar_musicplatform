# Generated by Django 4.1.2 on 2022-10-27 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='Social_link',
            new_name='social_link',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='Stage_Name',
            new_name='stage_name',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
