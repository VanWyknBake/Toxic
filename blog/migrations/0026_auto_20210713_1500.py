# Generated by Django 3.2.4 on 2021-07-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_post_ign'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='reason',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='uid',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
