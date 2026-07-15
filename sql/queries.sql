-- 1. Total Transactions

SELECT COUNT(*) AS Total_Transactions
FROM Transactions;

-- 2. Fraud Rate

SELECT
    Is_Fraud,
    COUNT(*) AS Total
FROM Transactions
GROUP BY Is_Fraud;

-- 3. Customer Segments

SELECT
    Customer_Segment,
    COUNT(*) AS Customers
FROM Customers
GROUP BY Customer_Segment
ORDER BY Customers DESC;

-- 4. Merchant Categories

SELECT
    Merchant_Category,
    COUNT(*) AS Merchants
FROM Merchants
GROUP BY Merchant_Category
ORDER BY Merchants DESC;

-- 5. Average Transaction Amount

SELECT
    ROUND(AVG(Amount),2) AS Average_Transaction
FROM Transactions;

-- 6. Fraud by Customer Segment

SELECT
    C.Customer_Segment,
    COUNT(*) AS Fraud_Transactions
FROM Transactions T
JOIN Customers C
ON T.Customer_ID = C.Customer_ID
WHERE T.Is_Fraud = 'Yes'
GROUP BY C.Customer_Segment
ORDER BY Fraud_Transactions DESC;

-- 7. Average Transaction by Merchant Category

SELECT
    M.Merchant_Category,
    ROUND(AVG(T.Amount),2) AS Average_Amount
FROM Transactions T
JOIN Merchants M
ON T.Merchant_ID = M.Merchant_ID
GROUP BY M.Merchant_Category
ORDER BY Average_Amount DESC;

-- 8. Top 10 Highest Transactions

SELECT
    Transaction_ID,
    Customer_ID,
    Amount
FROM Transactions
ORDER BY Amount DESC
LIMIT 10;

-- 9. Average Risk Score by Payment Channel

SELECT
    Payment_Channel,
    ROUND(AVG(Risk_Score),2) AS Average_Risk
FROM Transactions
GROUP BY Payment_Channel
ORDER BY Average_Risk DESC;

-- 9. Average Risk Score by Payment Channel

SELECT
    Payment_Channel,
    ROUND(AVG(Risk_Score),2) AS Average_Risk
FROM Transactions
GROUP BY Payment_Channel
ORDER BY Average_Risk DESC;

-- 10. Top Customers by Spending

SELECT
    Customer_ID,
    ROUND(SUM(Amount),2) AS Total_Spending
FROM Transactions
GROUP BY Customer_ID
ORDER BY Total_Spending DESC
LIMIT 10;