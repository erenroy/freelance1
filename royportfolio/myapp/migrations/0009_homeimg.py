# Generated by Django 5.0 on 2024-01-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_contact_name_remove_contact_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homeimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeimg', models.ImageField(blank=True, null=True, upload_to='home1')),
                ('blogtop', models.ImageField(blank=True, null=True, upload_to='home1')),
            ],
        ),
    ]
