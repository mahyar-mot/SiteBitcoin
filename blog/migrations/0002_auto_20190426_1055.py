# Generated by Django 2.2 on 2019-04-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, default='de.jpg', upload_to=''),
        ),
    ]
