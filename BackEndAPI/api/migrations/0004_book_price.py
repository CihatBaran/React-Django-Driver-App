# Generated by Django 3.1.7 on 2021-03-24 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
