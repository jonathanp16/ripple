# Generated by Django 4.2.4 on 2023-09-30 02:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_referral"),
    ]

    operations = [
        migrations.AddField(
            model_name="referral",
            name="message",
            field=models.TextField(blank=True, null=True),
        ),
    ]
