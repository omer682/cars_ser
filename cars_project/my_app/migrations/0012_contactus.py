# Generated by Django 4.2.2 on 2023-07-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_alter_person_age_alter_person_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('email', models.EmailField(max_length=155)),
                ('message', models.TextField(max_length=700)),
            ],
        ),
    ]