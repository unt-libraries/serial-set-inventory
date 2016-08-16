# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Congress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('congress_number', models.IntegerField()),
                ('begin_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house', models.CharField(max_length=2, choices=[(b'House', b'H'), (b'Senate', b'S')])),
                ('document_type', models.CharField(max_length=100)),
                ('document_name', models.CharField(unique=True, max_length=106)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution_name', models.CharField(max_length=255)),
                ('library_name', models.CharField(max_length=255)),
                ('address_2', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=255)),
                ('state', localflavor.us.models.USStateField()),
                ('zip_code', localflavor.us.models.USZipCodeField()),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=6, blank=True)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6, blank=True)),
                ('depository_number', models.CharField(max_length=255)),
                ('phone_number', localflavor.us.models.PhoneNumberField()),
                ('email_address', models.EmailField(max_length=254)),
                ('date_inventoried', models.DateField()),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departmental_edition', models.BooleanField(default=False)),
                ('note', models.CharField(max_length=255)),
                ('institution', models.ForeignKey(to='ssi.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_number', models.CharField(max_length=2, choices=[(b'1', b'1st'), (b'2', b'2nd'), (b'3', b'3rd'), (b'4', b'4th'), (b'5', b'5th'), (b'S', b'Special')])),
                ('begin_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('congress', models.ForeignKey(to='ssi.Congress')),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial_number', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('publication_numbers', models.CharField(max_length=255, blank=True)),
                ('annotation', models.CharField(max_length=255, blank=True)),
                ('not_issued', models.BooleanField(default=False)),
                ('document_type', models.ForeignKey(to='ssi.DocumentType')),
                ('session', models.ForeignKey(to='ssi.Session')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='volume',
            field=models.ForeignKey(to='ssi.Volume'),
        ),
        migrations.AddField(
            model_name='institution',
            name='volumes',
            field=models.ManyToManyField(to='ssi.Volume', through='ssi.Inventory'),
        ),
    ]
