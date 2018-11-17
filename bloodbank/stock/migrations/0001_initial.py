# Generated by Django 2.1.2 on 2018-11-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threshhold', models.IntegerField(default=0)),
                ('bloodgroup_A_plus', models.IntegerField(default=0)),
                ('bloodgroup_A_minus', models.IntegerField(default=0)),
                ('bloodgroup_B_plus', models.IntegerField(default=0)),
                ('bloodgroup_B_minus', models.IntegerField(default=0)),
                ('bloodgroup_O_plus', models.IntegerField(default=0)),
                ('bloodgroup_O_minus', models.IntegerField(default=0)),
                ('bloodgroup_AB_plus', models.IntegerField(default=0)),
                ('bloodgroup_AB_minus', models.IntegerField(default=0)),
            ],
        ),
    ]