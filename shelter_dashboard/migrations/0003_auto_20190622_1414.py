# Generated by Django 2.2.2 on 2019-06-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter_dashboard', '0002_auto_20190616_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('office', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='unburden',
            name='date_unburden',
            field=models.DateField(),
        ),
    ]
