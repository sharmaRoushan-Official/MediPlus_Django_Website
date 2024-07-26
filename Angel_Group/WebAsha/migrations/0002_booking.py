# Generated by Django 5.0.7 on 2024-07-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAsha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateTimeField()),
                ('disease', models.CharField(max_length=50)),
            ],
        ),
    ]
