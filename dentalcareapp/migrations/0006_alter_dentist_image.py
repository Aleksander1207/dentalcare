# Generated by Django 4.1.5 on 2023-02-02 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentalcareapp', '0005_alter_patient_dentist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentist',
            name='image',
            field=models.ImageField(null=True, upload_to='dentalcareapp/files/images/dentists'),
        ),
    ]
