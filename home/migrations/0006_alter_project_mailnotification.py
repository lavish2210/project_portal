# Generated by Django 3.2.5 on 2021-12-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_project_mailnotification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='MailNotification',
            field=models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF')], default='On', max_length=5),
        ),
    ]
