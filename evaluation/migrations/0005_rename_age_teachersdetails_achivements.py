# Generated by Django 3.2 on 2021-06-25 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0004_alter_teachersdetails_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachersdetails',
            old_name='Age',
            new_name='Achivements',
        ),
    ]