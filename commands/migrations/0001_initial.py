# Generated by Django 4.2.13 on 2024-06-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=255)),
                ('model_name', models.CharField(max_length=255)),
                ('applied', models.BooleanField(default=False)),
            ],
        ),
    ]
