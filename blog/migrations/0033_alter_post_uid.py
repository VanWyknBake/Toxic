# Generated by Django 3.2.4 on 2021-07-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_alter_post_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uid',
            field=models.CharField(blank=True, max_length=19, unique=True),
        ),
    ]