-- ===========================================
-- FinGuard Database Schema
-- ===========================================

CREATE TABLE Customers (
    Customer_ID TEXT PRIMARY KEY,
    Customer_Name TEXT,
    Age INTEGER,
    Gender TEXT,
    City TEXT,
    State TEXT,
    Customer_Segment TEXT,
    Occupation TEXT,
    Monthly_Income INTEGER,
    Account_Open_Year INTEGER,
    Preferred_Payment_Mode TEXT,
    Preferred_Device TEXT
);

CREATE TABLE Merchants (
    Merchant_ID TEXT PRIMARY KEY,
    Merchant_Name TEXT,
    Merchant_Category TEXT,
    City TEXT,
    State TEXT
);

CREATE TABLE Transactions (
    Transaction_ID TEXT PRIMARY KEY,
    Customer_ID TEXT,
    Merchant_ID TEXT,
    Transaction_Date DATE,
    Transaction_Time TIME,
    Transaction_Type TEXT,
    Amount REAL,
    Payment_Channel TEXT,
    Device_Type TEXT,
    Risk_Score INTEGER,
    Fraud_Type TEXT,
    Is_Fraud TEXT,

    FOREIGN KEY(Customer_ID)
        REFERENCES Customers(Customer_ID),

    FOREIGN KEY(Merchant_ID)
        REFERENCES Merchants(Merchant_ID)
);