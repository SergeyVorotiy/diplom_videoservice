# Generated by Django 4.2.3 on 2023-07-19 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svo_videoserviceapp', '0003_alter_vscomment_likes_alter_vsuser_black_list_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vscomment',
            name='ignored',
            field=models.BooleanField(default=False),
        ),
    ]
