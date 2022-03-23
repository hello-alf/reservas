# Generated by Django 3.2.12 on 2022-03-23 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was modified.', verbose_name='modified at')),
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.PositiveSmallIntegerField(default=1)),
                ('floor', models.PositiveSmallIntegerField(default=1)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]