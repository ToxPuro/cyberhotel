# Generated by Django 3.1.2 on 2020-11-15 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='msg',
            new_name='content',
        ),
    ]
