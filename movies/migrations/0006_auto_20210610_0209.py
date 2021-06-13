# Generated by Django 3.1.7 on 2021-06-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20210610_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('action', 'Action'), ('adventure', 'Adventure'), ('comedy', 'Comedy'), ('crime and mystery', 'Crime & Mystery'), ('documentary', 'Documentary'), ('family', 'Family'), ('fantasy', 'Fantasy'), ('historical', 'Historical'), ('horror', 'Horror'), ('romance', 'Romance'), ('sci_fi', 'Science fiction'), ('superhero', 'Superhero'), ('thriller', 'Thriller'), ('western', 'Western')], max_length=20),
        ),
    ]
