# Generated by Django 4.2.5 on 2023-09-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mne_gui_app', '0002_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('detail', models.CharField(max_length=500)),
            ],
        ),
    ]