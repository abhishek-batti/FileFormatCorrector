# Generated by Django 4.1 on 2023-09-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fileformatter", "0002_infile_filename"),
    ]

    operations = [
        migrations.AlterField(
            model_name="infile",
            name="f",
            field=models.FileField(
                blank=True, null=True, upload_to="D:\\FormatCorrectionProject\\pool"
            ),
        ),
    ]
