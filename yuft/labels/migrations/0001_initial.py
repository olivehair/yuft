# Generated by Django 4.0.6 on 2022-08-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation datetime of the object', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='modification datetime of the object', verbose_name='updated at')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('brand', models.CharField(max_length=128, verbose_name='brand')),
                ('owner', models.CharField(max_length=128, verbose_name='owner')),
                ('serial_number', models.BigIntegerField(db_index=True, unique=True, verbose_name='serial number')),
                ('signature', models.TextField(verbose_name='signature')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
