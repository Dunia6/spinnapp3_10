# Generated by Django 5.0.3 on 2024-04-02 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_articleimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Category',
            new_name='category',
        ),
    ]
