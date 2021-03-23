# Generated by Django 3.1.5 on 2021-03-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210303_1741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['id', '-title']},
        ),
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.AddField(
            model_name='project',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='project/pdf/'),
        ),
        migrations.AddField(
            model_name='project',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to='project/thumb/'),
        ),
    ]