# Generated by Django 4.2.16 on 2024-11-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='title')),
                ('price', models.FloatField(verbose_name='price')),
                ('content', models.TextField(verbose_name='content')),
                ('user', models.CharField(max_length=20, verbose_name='user')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date')),
            ],
            options={
                'verbose_name': 'announcement',
                'verbose_name_plural': 'announcements',
                'ordering': ['date'],
            },
        ),
    ]
