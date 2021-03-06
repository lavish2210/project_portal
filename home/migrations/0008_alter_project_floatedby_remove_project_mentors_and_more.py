# Generated by Django 4.0.1 on 2022-01-09 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_alter_project_mailnotification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='FloatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FloatedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='project',
            name='Mentors',
        ),
        migrations.AddField(
            model_name='project',
            name='Mentors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Mentors', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
