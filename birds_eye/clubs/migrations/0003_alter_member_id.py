# Generated by Django 4.1.2 on 2022-10-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clubs", "0002_club_member_alter_groupmember_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="id",
            field=models.IntegerField(
                help_text="ID of the student", primary_key=True, serialize=False
            ),
        ),
    ]