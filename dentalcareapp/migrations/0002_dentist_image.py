# Generated by Django 4.1.5 on 2023-01-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentalcareapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentist',
            name='image',
            field=models.ImageField(default=None, upload_to='dentalcareapp/files/images'),
            preserve_default=False,
        ),
    ]
