# Generated by Django 5.1.7 on 2025-03-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_subscription_reminder_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='reminder_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
