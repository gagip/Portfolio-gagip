# Generated by Django 3.1.5 on 2021-03-20 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210310_0018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-id', '-title']},
        ),
    ]
