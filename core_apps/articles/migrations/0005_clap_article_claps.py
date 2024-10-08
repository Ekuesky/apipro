# Generated by Django 4.1.7 on 2024-08-20 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("articles", "0004_alter_articleview_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Clap",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articles.article",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Clap",
                "verbose_name_plural": "Claps",
                "ordering": ["-created_at"],
                "unique_together": {("article", "user")},
            },
        ),
        migrations.AddField(
            model_name="article",
            name="claps",
            field=models.ManyToManyField(
                related_name="clapped_articles",
                through="articles.Clap",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
