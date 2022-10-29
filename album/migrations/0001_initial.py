# Generated by Django 4.1.2 on 2022-10-27 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0002_rename_social_link_artist_social_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(default='New Album', max_length=200, verbose_name='New Album')),
                ('creation_time', models.DateTimeField(unique=True, verbose_name='time created')),
                ('release_time', models.DateTimeField(verbose_name='publish time')),
                ('album_cost', models.DecimalField(decimal_places=2, max_digits=20)),
                ('artist_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.artist')),
            ],
        ),
    ]
