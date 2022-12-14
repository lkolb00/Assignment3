# Generated by Django 4.1.2 on 2022-11-02 03:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0003_auto_20221020_1536"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer", models.CharField(max_length=50)),
                ("category", models.EmailField(max_length=100)),
                ("description", models.CharField(max_length=20)),
                ("location", models.CharField(max_length=100)),
                ("setup_time", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "cleanup_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("service_charge", models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(name="Club",),
    ]
