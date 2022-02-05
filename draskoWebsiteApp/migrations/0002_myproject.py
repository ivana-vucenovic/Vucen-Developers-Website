# Generated by Django 3.2.7 on 2022-02-01 18:57

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('draskoWebsiteApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('services', models.ManyToManyField(related_name='projects', to='draskoWebsiteApp.User')),
            ],
            managers=[
                ('my_projects', django.db.models.manager.Manager()),
            ],
        ),
    ]