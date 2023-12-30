# Generated by Django 4.2.5 on 2023-09-19 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentalcareapp', '0009_remove_dentist_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dentalcareapp/files/images/dentists'),
        ),
    ]