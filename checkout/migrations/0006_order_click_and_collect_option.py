# Generated by Django 3.0.6 on 2020-07-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_delivery_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='click_and_collect_option',
            field=models.CharField(blank=True, choices=[("Ben's Hardware", "Ben's Hardware"), ('Pembroke Park Post Office', 'Pembroke Park Post Office')], max_length=80, null=True),
        ),
    ]
