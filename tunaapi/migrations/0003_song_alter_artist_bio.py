# Generated by Django 4.2.8 on 2023-12-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunaapi', '0002_alter_artist_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('album', models.CharField(max_length=25)),
                ('length', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.TextField(),
        ),
    ]
