# Generated by Django 4.1 on 2023-03-08 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_word_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='postfixess',
            new_name='postfixes',
        ),
    ]
