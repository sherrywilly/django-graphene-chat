# Generated by Django 3.2.3 on 2021-05-29 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='messages',
            field=models.ManyToManyField(blank=True, to='chat.Message'),
        ),
    ]
