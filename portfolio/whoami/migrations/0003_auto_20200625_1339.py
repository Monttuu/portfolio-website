# Generated by Django 3.0.6 on 2020-06-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoami', '0002_auto_20200625_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='me',
            name='text_workExperience',
            field=models.TextField(),
        ),
    ]
