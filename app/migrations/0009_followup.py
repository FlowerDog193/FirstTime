# Generated by Django 3.2.12 on 2022-02-25 03:09

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_a001_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=app.models.handle_upload_follow_ups)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followups', to='app.a001')),
            ],
            options={
                'verbose_name': 'フォローアップ',
                'verbose_name_plural': 'フォローアップ',
            },
        ),
    ]
