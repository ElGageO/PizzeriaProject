# Generated by Django 3.0.5 on 2022-05-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_comment_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
