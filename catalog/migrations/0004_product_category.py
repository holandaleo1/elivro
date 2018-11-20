# Generated by Django 2.1.3 on 2018-11-18 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='catalog.Category'),
            preserve_default=False,
        ),
    ]
