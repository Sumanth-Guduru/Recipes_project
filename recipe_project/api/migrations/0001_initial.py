# Generated by Django 5.0.7 on 2024-07-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('idMeal', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('strMeal', models.CharField(max_length=100)),
                ('strInstructions', models.TextField()),
                ('strMealThumb', models.URLField()),
            ],
        ),
    ]