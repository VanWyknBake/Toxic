# Generated by Django 3.2.4 on 2021-06-29 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default='', upload_to=''),
        ),
    ]
