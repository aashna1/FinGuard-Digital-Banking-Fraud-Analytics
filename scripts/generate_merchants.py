"""
FinGuard - Merchant Data Generator
Creates realistic merchant information.
"""

import random
import pandas as pd

from config import (
    NUM_MERCHANTS
)

merchant_categories = {

    "Shopping": [
        "Amazon India",
        "Flipkart",
        "Myntra",
        "Ajio",
        "Reliance Digital",
        "Croma"
    ],

    "Food": [
        "Swiggy",
        "Zomato",
        "Domino's",
        "McDonald's",
        "Burger King",
        "Haldiram"
    ],

    "Grocery": [
        "DMart",
        "Reliance Fresh",
        "BigBasket",
        "Nature's Basket",
        "Spencer's"
    ],

    "Fuel": [
        "Indian Oil",
        "HP Petrol Pump",
        "Bharat Petroleum"
    ],

    "Healthcare": [
        "Apollo Pharmacy",
        "MedPlus",
        "Tata 1mg"
    ],

    "Travel": [
        "Uber",
        "Ola",
        "IRCTC",
        "MakeMyTrip"
    ],

    "Entertainment": [
        "BookMyShow",
        "PVR",
        "INOX"
    ],

    "Utilities": [
        "Airtel",
        "Jio",
        "BSES",
        "Tata Power"
    ]
}

cities = [

    ("Delhi","Delhi"),

    ("Mumbai","Maharashtra"),

    ("Bengaluru","Karnataka"),

    ("Hyderabad","Telangana"),

    ("Chennai","Tamil Nadu"),

    ("Pune","Maharashtra"),

    ("Ahmedabad","Gujarat"),

    ("Jaipur","Rajasthan"),

    ("Lucknow","Uttar Pradesh"),

    ("Kolkata","West Bengal")

]

def generate_merchants():

    merchants = []

    merchant_id = 1

    for category, merchant_list in merchant_categories.items():

        for merchant in merchant_list:

            city, state = random.choice(cities)

            merchants.append({

                "Merchant_ID": f"MER{merchant_id:03d}",

                "Merchant_Name": merchant,

                "Merchant_Category": category,

                "City": city,

                "State": state

            })

            merchant_id += 1

    df = pd.DataFrame(merchants)
    from config import (
    NUM_MERCHANTS,
    MERCHANTS_FILE
)
    
    df.to_csv(MERCHANTS_FILE, index=False)

    print("Merchant dataset generated successfully.")

if __name__ == "__main__":
    generate_merchants()