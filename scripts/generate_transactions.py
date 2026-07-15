"""
FinGuard - Transaction Generator
Creates realistic banking transactions.
"""

import random
from datetime import datetime, timedelta

import pandas as pd

from config import (
    NUM_TRANSACTIONS,
    CUSTOMERS_FILE,
    MERCHANTS_FILE,
    TRANSACTIONS_FILE
)

customers = pd.read_csv(CUSTOMERS_FILE)
merchants = pd.read_csv(MERCHANTS_FILE)

transaction_types = [
    "UPI",
    "Debit Card",
    "Credit Card",
    "Net Banking",
    "ATM Withdrawal",
    "NEFT",
    "RTGS",
    "IMPS"
]

fraud_types = [
    "None",
    "Card Skimming",
    "Phishing",
    "SIM Swap",
    "Identity Theft",
    "Account Takeover"
]

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

days_between = (end_date - start_date).days

def calculate_risk(customer, amount, transaction_time):

    risk_score = random.randint(5, 25)

    fraud_type = "None"

    # Rule 1 - High Amount
    if amount > 80000:
        risk_score += 35

    # Rule 2 - Night Transactions
    if transaction_time.hour >= 0 and transaction_time.hour <= 4:
        risk_score += 20

    # Rule 3 - Senior Citizens with High Amount
    if (
        customer["Customer_Segment"] == "Senior Citizen"
        and amount > 40000
    ):
        risk_score += 25

    # Final Decision
    if risk_score >= 60:

        fraud_type = random.choice([
            "Card Skimming",
            "Phishing",
            "SIM Swap",
            "Identity Theft",
            "Account Takeover"
        ])

        is_fraud = "Yes"

    else:

        is_fraud = "No"

    risk_score = min(risk_score, 100)

    return risk_score, fraud_type, is_fraud

def generate_transaction(transaction_number):

    customer = customers.sample(1).iloc[0]

    merchant = merchants.sample(1).iloc[0]

    random_days = random.randint(0, days_between)

    transaction_datetime = start_date + timedelta(days=random_days)

    transaction_time = transaction_datetime.replace(
        hour=random.randint(0, 23),
        minute=random.randint(0, 59),
        second=random.randint(0, 59)
    )

    segment = customer["Customer_Segment"]

    if segment == "Student":
        amount = random.randint(50, 3000)

    elif segment == "Salaried":
        amount = random.randint(200, 30000)

    elif segment == "Business":
        amount = random.randint(500, 100000)

    else:
        amount = random.randint(100, 15000)

    risk_score, fraud_type, is_fraud = calculate_risk(
        customer,
        amount,
        transaction_time
    )
    return {

        "Transaction_ID": f"TXN{transaction_number:06d}",

        "Customer_ID": customer["Customer_ID"],

        "Merchant_ID": merchant["Merchant_ID"],

        "Transaction_Date": transaction_time.strftime("%Y-%m-%d"),

        "Transaction_Time": transaction_time.strftime("%H:%M:%S"),

        "Transaction_Type": random.choice(transaction_types),

        "Amount": amount,

        "Payment_Channel": customer["Preferred_Payment_Mode"],

        "Device_Type": customer["Preferred_Device"],

        "Risk_Score": risk_score,

        "Fraud_Type": fraud_type,

        "Is_Fraud": is_fraud
    }

def generate_transactions():

    transactions = []

    for i in range(1, NUM_TRANSACTIONS + 1):

        transactions.append(
            generate_transaction(i)
        )

    df = pd.DataFrame(transactions)

    df.to_csv(
        TRANSACTIONS_FILE,
        index=False
    )

    print(f"{NUM_TRANSACTIONS} transactions generated successfully.")

if __name__ == "__main__":
    generate_transactions()