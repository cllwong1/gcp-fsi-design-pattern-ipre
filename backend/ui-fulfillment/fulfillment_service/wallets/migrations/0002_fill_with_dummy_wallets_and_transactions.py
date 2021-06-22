# Generated by Django 3.2.3 on 2021-06-07 13:20


from django.db import migrations
from fulfillment_service.utils.migrations import load_statements


class Migration(migrations.Migration):
    dependencies = [
        ('wallets', '0001_initial'),
        ('users', '0002_fill_with_dummy_users'),
    ]

    operations = [
        migrations.RunSQL(
            load_statements('wallets/sql/wallets.sql'),
            load_statements('wallets/sql/drop_wallets.sql'),
        ),
        migrations.RunSQL(
            load_statements('wallets/sql/transactions.sql'),
            load_statements('wallets/sql/drop_transactions.sql'),
        ),
    ]