# Generated by Django 3.2.3 on 2021-06-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricityDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.DecimalField(decimal_places=4, max_digits=1000)),
                ('voltage', models.DecimalField(decimal_places=4, max_digits=1000)),
                ('power', models.DecimalField(decimal_places=4, max_digits=1000)),
            ],
        ),
    ]
