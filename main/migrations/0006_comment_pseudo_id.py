# Generated by Django 4.1.2 on 2022-10-21 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_comment_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pseudo_id',
            field=models.IntegerField(null=True),
        ),
    ]
