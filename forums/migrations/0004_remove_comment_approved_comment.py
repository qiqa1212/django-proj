# Generated by Django 4.1.7 on 2023-03-27 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_comment_delete_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]
