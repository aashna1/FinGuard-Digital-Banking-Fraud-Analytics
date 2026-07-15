"""
FinGuard - Customer Data Generator
Generates realistic banking customer data.
"""

import random
from faker import Faker
import pandas as pd

from config import (
    NUM_CUSTOMERS,
    CUSTOMERS_FILE
)

fake = Faker("en_IN")

customer_segments = [
    "Student",
    "Salaried",
    "Business",
    "Senior Citizen"
]

payment_methods = [
    "UPI",
    "Debit Card",
    "Credit Card",
    "Net Banking"
]

device_types = [
    "Mobile",
    "Laptop",
    "Tablet"
]

occupations = {
    "Student": [
        "College Student",
        "Engineering Student",
        "MBA Student",
        "Medical Student"
    ],

    "Salaried": [
        "Software Engineer",
        "Teacher",
        "Doctor",
        "Chartered Accountant",
        "Bank Manager",
        "Data Analyst",
        "Marketing Executive",
        "Civil Engineer",
        "HR Manager"
    ],

    "Business": [
        "Business Owner",
        "Restaurant Owner",
        "Retailer",
        "Trader",
        "Consultant"
    ],

    "Senior Citizen": [
        "Retired Government Officer",
        "Retired Teacher",
        "Retired Banker",
        "Retired Army Officer"
    ]
}

cities = [
    ("Delhi", "Delhi"),
    ("Mumbai", "Maharashtra"),
    ("Bengaluru", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Chennai", "Tamil Nadu"),
    ("Kolkata", "West Bengal"),
    ("Pune", "Maharashtra"),
    ("Ahmedabad", "Gujarat"),
    ("Jaipur", "Rajasthan"),
    ("Lucknow", "Uttar Pradesh")
]

def generate_customers():
    customers = []

    for i in range(1, NUM_CUSTOMERS + 1):

        city, state = random.choice(cities)

        segment = random.choice(customer_segments)

        if segment == "Student":
            age = random.randint(18, 25)
        elif segment == "Salaried":
            age = random.randint(23, 58)
        elif segment == "Business":
            age = random.randint(28, 65)
        else:
            age = random.randint(60, 85)

        customer = {
                "Customer_ID": f"CUST{i:04d}",
                "Customer_Name": fake.name(),
                "Age": age,
                "Gender": random.choice(["Male", "Female"]),
                "City": city,
                "State": state,
                "Customer_Segment": segment,

                "Occupation": random.choice(occupations[segment]),

                "Monthly_Income": random.randint(15000, 250000),

                "Account_Open_Year": random.randint(2012, 2026),

                "Preferred_Payment_Mode": random.choice(payment_methods),

                "Preferred_Device": random.choice(device_types)
        }
        
        customers.append(customer)

    df = pd.DataFrame(customers)

    df.to_csv(CUSTOMERS_FILE, index=False)

    print(f"Generated {NUM_CUSTOMERS} customers successfully.")

if __name__ == "__main__":
    generate_customers()