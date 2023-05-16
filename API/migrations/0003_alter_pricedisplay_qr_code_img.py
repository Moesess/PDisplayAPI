# Generated by Django 4.1.7 on 2023-05-16 20:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_pricedisplay_qr_code_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedisplay',
            name='qr_code_img',
            field=models.ImageField(upload_to='API/qr_codes/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]
