# Generated by Django 4.1 on 2022-09-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Announcement",
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
                ("title", models.CharField(max_length=50)),
                ("host", models.CharField(max_length=50)),
                ("host_title", models.CharField(max_length=100)),
                ("body", models.TextField(max_length=500)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created"],},
        ),
        migrations.CreateModel(
            name="Commission",
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
                ("name", models.CharField(max_length=100)),
                ("chair", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Lesson",
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
                ("name", models.CharField(max_length=50)),
                ("tutor", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=100)),
                ("host", models.CharField(max_length=100)),
                ("body", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="")),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created"],},
        ),
        migrations.CreateModel(
            name="Sponsor",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
    ]
