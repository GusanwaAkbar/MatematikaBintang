# Generated by Django 4.2.4 on 2023-08-26 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0006_alter_subscriptionrequest_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionrequest',
            name='status',
            field=models.CharField(default='Menunggu Pembayaran', max_length=100),
        ),
    ]
