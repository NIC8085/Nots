# Generated by Django 4.2.2 on 2023-06-06 15:30

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=15)),
            ],
            managers=[
                ('priorityManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=50)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='NotsApp.priority')),
            ],
            managers=[
                ('noteManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
