# Generated by Django 2.1.2 on 2018-12-07 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBankName',
            fields=[
                ('bloodbankid', models.AutoField(primary_key=True, serialize=False)),
                ('bloodbankname', models.CharField(max_length=30)),
                ('latitude', models.FloatField(max_length=30)),
                ('longitude', models.FloatField(max_length=30)),
            ],
        ),
    ]