# Generated by Django 3.1.7 on 2021-03-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_headline', models.CharField(max_length=64)),
                ('story_category', models.CharField(max_length=100)),
                ('story_region', models.CharField(max_length=100)),
                ('story_author_name', models.CharField(max_length=100)),
                ('story_date', models.DateTimeField(auto_now_add=True)),
                ('story_details', models.CharField(max_length=1000)),
            ],
        ),
    ]