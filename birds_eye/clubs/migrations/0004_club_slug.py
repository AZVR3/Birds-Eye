# Generated by Django 4.1.2 on 2022-10-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clubs", "0003_alter_member_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="club",
            name="slug",
            field=models.SlugField(allow_unicode=True, null=True, unique=True),
        ),
    ]