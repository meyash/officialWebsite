# Generated by Django 3.0 on 2019-12-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0004_remove_member_team"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="dev_url",
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="github_url",
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="linkedin_url",
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="medium_url",
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="twitter_url",
            field=models.URLField(blank=True),
        ),
    ]