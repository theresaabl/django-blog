# Generated by Django 4.2.17 on 2025-01-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_rename_created_on_about_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='about',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]