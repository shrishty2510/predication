# Generated by Django 3.2.7 on 2022-04-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_feedback_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(blank=True, default='no feedback', null=True),
        ),
    ]
