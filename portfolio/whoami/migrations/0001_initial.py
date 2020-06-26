# Generated by Django 3.0.6 on 2020-06-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictures/')),
                ('title_shortInfo', models.CharField(max_length=200)),
                ('text_shortInfo', models.TextField()),
                ('title_education', models.CharField(max_length=200)),
                ('text_education', models.TextField()),
                ('title_thesis', models.CharField(max_length=200)),
                ('text_thesis', models.TextField()),
                ('title_workExperience', models.CharField(max_length=200)),
                ('text_workExperience', models.TextField()),
                ('title_currentPosition', models.CharField(max_length=200)),
                ('text_currentPosition', models.TextField()),
                ('title_skills', models.CharField(max_length=200)),
                ('text_skills', models.TextField()),
                ('title_codingTechnologies', models.CharField(max_length=200)),
                ('text_codingTechnologies', models.TextField()),
                ('title_hobbies', models.CharField(max_length=200)),
                ('text_hobbies', models.TextField()),
            ],
        ),
    ]
