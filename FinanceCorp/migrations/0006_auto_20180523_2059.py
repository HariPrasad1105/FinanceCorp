# Generated by Django 2.0.4 on 2018-05-23 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceCorp', '0005_auto_20180523_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payeepaymentdetails',
            old_name='payeeId',
            new_name='payeeID',
        ),
    ]