# Generated by Django 2.0.6 on 2018-08-31 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.CharField(help_text='Logo of Album must be an "url"', max_length=1000),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_title',
            field=models.CharField(help_text='Album Name', max_length=500),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(help_text='Artist Name who Song the Songs', max_length=250),
        ),
        migrations.AlterField(
            model_name='album',
            name='genere',
            field=models.CharField(help_text='Genere: Classic, Rock etc.', max_length=100),
        ),
        migrations.AddField(
            model_name='comments',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album'),
        ),
    ]
