# Generated by Django 4.0 on 2022-01-18 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_profile_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='github_link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linked_in_link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='portfolio_link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
