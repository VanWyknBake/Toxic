# Generated by Django 3.2 on 2021-07-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ign',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]