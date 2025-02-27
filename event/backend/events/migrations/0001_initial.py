# Generated by Django 4.2.16 on 2024-09-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('date', models.CharField(max_length=50, verbose_name='Date')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('description', models.TextField(verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
            ],
        ),
    ]
