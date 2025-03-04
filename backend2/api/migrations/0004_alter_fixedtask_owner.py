# Generated by Django 5.1.6 on 2025-02-26 07:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_fixedtask_enddate_alter_fixedtask_startingdate_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="fixedtask",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fixedTask_owner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
