# Generated by Django 4.1.7 on 2023-04-19 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_alter_product_options_pricedisplay_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'get_latest_by': '-last_modified', 'ordering': ['name', '-last_modified'], 'verbose_name': 'Product'},
        ),
    ]
