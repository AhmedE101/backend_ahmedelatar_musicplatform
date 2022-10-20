# Generated by Django 4.1.2 on 2022-10-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_Cost',
            new_name='album_cost',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='album_Name',
            new_name='album_name',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='artist_Fk',
            new_name='artist_fk',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='creation_Time',
            new_name='creation_time',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='release_Time',
            new_name='release_time',
        ),
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
        migrations.AddField(
            model_name='album',
            name='album_is_approved',
            field=models.BooleanField(default=True, help_text='Approve the album if its name is not explicit'),
        ),
    ]