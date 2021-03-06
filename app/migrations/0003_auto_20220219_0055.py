# Generated by Django 3.2.12 on 2022-02-19 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220218_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='a001',
            name='organisation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.userprofile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='a001',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.agent'),
        ),
    ]
