# Generated by Django 3.1.6 on 2021-02-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_merged'),
    ]

    operations = [
        migrations.AddField(
            model_name='frame',
            name='mask',
            field=models.ImageField(default='d.png', upload_to='mask_img'),
        ),
    ]