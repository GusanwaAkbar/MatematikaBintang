# Generated by Django 3.2 on 2021-05-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0003_alter_materi_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='materi',
            name='kelas',
            field=models.ManyToManyField(to='blog_post.kelas'),
        ),
    ]
