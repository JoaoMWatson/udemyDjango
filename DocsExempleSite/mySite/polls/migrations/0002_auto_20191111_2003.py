# Generated by Django 2.2.7 on 2019-11-11 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_next',
            new_name='question_text',
        ),
    ]