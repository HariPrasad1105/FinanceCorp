# Generated by Django 2.0.4 on 2018-05-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceCorp', '0002_remove_lender_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='lender',
            name='type',
            field=models.CharField(default='lender', max_length=10),
        ),
    ]
