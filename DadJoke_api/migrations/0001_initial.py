# Generated by Django 2.2 on 2020-04-24 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadJoke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joke_text', models.CharField(max_length=255)),
                ('groan_factor', models.IntegerField()),
            ],
        ),
    ]
