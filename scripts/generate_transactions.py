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

def calculate_risk(customer, merchant, amount, transaction_time):

    risk_score = random.randint(5, 25)
    fraud_type = "None"

    # Rule 1 - Credit Card transactions
    if customer["Preferred_Payment_Mode"] == "Credit Card":
        risk_score += 12

    # Rule 2 - Mobile device
    if customer["Preferred_Device"] == "Mobile":
        risk_score += 8

    # Rule 3 - Shopping & Electronics merchants
    if merchant["Merchant_Category"] in [
        "Shopping",
        "Electronics"
    ]:
        risk_score += 15

    # Rule 4 - High amount
    if amount > 50000:
        risk_score += 20

    if amount > 80000:
        risk_score += 15

    # Rule 5 - Late night
    if transaction_time.hour >= 22 or transaction_time.hour <= 4:
        risk_score += 18

    # Rule 6 - Senior Citizen
    if (
        customer["Customer_Segment"] == "Senior Citizen"
        and amount > 30000
    ):
        risk_score += 15

    # Rule 7 - Business customers
    if (
        customer["Customer_Segment"] == "Business"
        and amount > 75000
    ):
        risk_score += 10

    # Rule 8 - Different customer and merchant city
    if customer["City"] != merchant["City"]:
        risk_score += 10

    fraud_probability = 0

    if risk_score >= 85:
        fraud_probability = 0.70

    elif risk_score >= 70:
        fraud_probability = 0.35

    elif risk_score >= 55:
        fraud_probability = 0.15

    elif risk_score >= 40:
        fraud_probability = 0.03

    is_fraud = (
        "Yes"
        if random.random() < fraud_probability
        else "No"
    )

    if is_fraud == "Yes":
        fraud_type = random.choice([
            "Card Skimming",
            "Phishing",
            "SIM Swap",
            "Identity Theft",
            "Account Takeover"
        ])

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
        merchant,
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