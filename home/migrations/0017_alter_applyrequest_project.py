# Generated by Django 4.0 on 2022-03-06 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_project_applyrequest_applyrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyrequest',
            name='Project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.project'),
        ),
    ]
