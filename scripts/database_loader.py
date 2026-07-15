"""
FinGuard Database Loader
Creates SQLite database and imports CSV files.
"""

import sqlite3
import pandas as pd

from config import (
    DATABASE_FILE,
    CUSTOMERS_FILE,
    MERCHANTS_FILE,
    TRANSACTIONS_FILE
)

def create_database():

    conn = sqlite3.connect(DATABASE_FILE)

    customers = pd.read_csv(CUSTOMERS_FILE)
    merchants = pd.read_csv(MERCHANTS_FILE)
    transactions = pd.read_csv(TRANSACTIONS_FILE)

    customers.to_sql(
        "Customers",
        conn,
        if_exists="replace",
        index=False
    )

    merchants.to_sql(
        "Merchants",
        conn,
        if_exists="replace",
        index=False
    )

    transactions.to_sql(
        "Transactions",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Database created successfully.")

if __name__ == "__main__":
    create_database()

