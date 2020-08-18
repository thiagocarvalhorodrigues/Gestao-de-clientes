# Generated by Django 3.0.8 on 2020-07-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Historia', models.TextField()),
                ('Idade', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='clients_photos')),
            ],
        ),
    ]