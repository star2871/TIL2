# Generated by Django 4.0.6 on 2022-08-25 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.genre')),
            ],
        ),
    ]
