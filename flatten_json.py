import json
import sqlite3

# Sample JSON data
data = {
    "customers": [
        {
            "customer_id": 101,
            "name": "John Doe",
            "email": "johndoe@example.com",
            "phone": "+1-555-1234",
            "transactions": [
                {
                    "transaction_id": "TXN001",
                    "amount": 250.75,
                    "currency": "USD",
                    "date": "2025-02-26T14:30:00Z",
                    "payment_method": "Credit Card"
                },
                {
                    "transaction_id": "TXN002",
                    "amount": 89.50,
                    "currency": "USD",
                    "date": "2025-02-20T10:15:00Z",
                    "payment_method": "PayPal"
                }
            ]
        },
        {
            "customer_id": 102,
            "name": "Jane Smith",
            "email": "janesmith@example.com",
            "phone": "+1-555-5678",
            "transactions": [
                {
                    "transaction_id": "TXN003",
                    "amount": 500.00,
                    "currency": "USD",
                    "date": "2025-02-25T18:00:00Z",
                    "payment_method": "Debit Card"
                }
            ]
        }
    ]
}

# Create SQLite in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create tables for customers and transactions
cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT
)
""")

cursor.execute("""
CREATE TABLE transactions (
    transaction_id TEXT PRIMARY KEY,
    amount REAL,
    currency TEXT,
    date TEXT,
    payment_method TEXT,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

# Insert data into customers and transactions tables
for customer in data["customers"]:
    cursor.execute("INSERT INTO customers (customer_id, name, email, phone) VALUES (?, ?, ?, ?)", 
                   (customer["customer_id"], customer["name"], customer["email"], customer["phone"]))
    
    for transaction in customer["transactions"]:
        cursor.execute("INSERT INTO transactions (transaction_id, amount, currency, date, payment_method, customer_id) VALUES (?, ?, ?, ?, ?, ?)",
                       (transaction["transaction_id"], transaction["amount"], transaction["currency"], 
                        transaction["date"], transaction["payment_method"], customer["customer_id"]))

# Query to flatten the data
flatten_query = """
SELECT 
    c.customer_id, c.name, c.email, c.phone, 
    t.transaction_id, t.amount, t.currency, t.date, t.payment_method
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
"""

cursor.execute(flatten_query)
flattened_data = cursor.fetchall()

# Convert results to a structured list
columns = ["customer_id", "name", "email", "phone", "transaction_id", "amount", "currency", "date", "payment_method"]
result = [dict(zip(columns, row)) for row in flattened_data]

# Print and save the flattened JSON data
print(json.dumps(result, indent=4))

with open("flattened_data.json", "w") as f:
    json.dump(result, f, indent=4)

# Close the database connection
conn.close()
