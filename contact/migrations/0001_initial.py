# Generated by Django 2.2.3 on 2019-07-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('cnt_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_name', models.CharField(max_length=50)),
                ('from_email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=1150)),
            ],
        ),
    ]