# Generated by Django 2.1.9 on 2020-12-01 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
    ]
