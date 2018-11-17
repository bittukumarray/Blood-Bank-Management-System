# Generated by Django 2.1.2 on 2018-11-05 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PathLabs',
            fields=[
                ('pathlabid', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(choices=[('Chennai', 'Chennai'), ('Bangalore', 'Bangalore'), ('Patna', 'Patna'), ('Mumbai', 'Mumbai'), ('Hyderabad', 'Hyderabad'), ('Kolkata', 'Kolkata'), ('Delhi', 'Delhi'), ('Jamshedpur', 'Jamshedpur')], max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('ratings', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PathLabUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=1000)),
                ('feedback', models.CharField(blank=True, max_length=1000)),
                ('pathlab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathlab.PathLabs')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
