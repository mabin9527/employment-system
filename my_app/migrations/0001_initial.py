# Generated by Django 3.2.19 on 2023-05-08 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=64)),
                ('age', models.IntegerField(verbose_name='age')),
                ('account', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='balance')),
                ('create_time', models.DateTimeField(verbose_name='hire date')),
                ('gender', models.SmallIntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.department')),
            ],
        ),
    ]
