# Generated by Django 4.1.5 on 2024-07-01 05:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainlogin", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="login",
            name="f_name",
            field=models.CharField(
                blank=True, db_column="F_NAME", max_length=150, null=True
            ),
        ),
        migrations.AddField(
            model_name="login",
            name="l_name",
            field=models.CharField(
                blank=True, db_column="L_NAME", max_length=150, null=True
            ),
        ),
        migrations.AddField(
            model_name="login",
            name="user_type",
            field=models.CharField(
                blank=True, db_column="User_Type", max_length=50, null=True
            ),
        ),
    ]
