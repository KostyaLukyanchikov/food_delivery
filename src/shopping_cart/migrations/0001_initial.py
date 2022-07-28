# Generated by Django 4.0.6 on 2022-07-28 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartPosition',
            fields=[
                ('dish', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='menu.dish')),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]