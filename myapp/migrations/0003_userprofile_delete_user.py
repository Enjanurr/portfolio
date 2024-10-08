# Generated by Django 5.0.7 on 2024-08-13 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
