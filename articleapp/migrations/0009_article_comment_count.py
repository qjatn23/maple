# Generated by Django 5.1.4 on 2024-12-24 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0008_remove_article_comment_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
    ]