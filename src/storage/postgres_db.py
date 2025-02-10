import psycopg2
import pandas as pd

# Database connection details
DB_NAME = "ecommerce_db"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        return conn
    except Exception as e:
        print("Database connection failed:", e)
        return None

# Create tables
def create_tables():
    conn = connect_db()
    if conn is None:
        return
    
    cursor = conn.cursor()
    
    orders_table = """
    CREATE TABLE IF NOT EXISTS orders (
        order_id SERIAL PRIMARY KEY,
        product VARCHAR(255),
        category VARCHAR(100),
        price DECIMAL(10,2),
        discounted_price DECIMAL(10,2),
        order_date DATE,
        customer_id INT
    );
    """
    
    customers_table = """
    CREATE TABLE IF NOT EXISTS customers (
        customer_id SERIAL PRIMARY KEY,
        customer_name VARCHAR(255),
        email VARCHAR(255) UNIQUE,
        total_orders INT,
        total_spent DECIMAL(10,2)
    );
    """
    
    cursor.execute(orders_table)
    cursor.execute(customers_table)
    conn.commit()
    cursor.close()
    conn.close()
    print("Tables created successfully!")

# Load data from CSV into database
def load_data():
    conn = connect_db()
    if conn is None:
        return
    
    cursor = conn.cursor()
    
    # Load orders data
    orders_df = pd.read_csv("storage/transformed_data.csv")
    for _, row in orders_df.iterrows():
        cursor.execute(
            "INSERT INTO orders (order_id, product, category, price, discounted_price, order_date, customer_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            tuple(row)
        )
    
    # Load customers data
    customers_df = pd.read_csv("storage/transformed_customers.csv")
    for _, row in customers_df.iterrows():
        cursor.execute(
            "INSERT INTO customers (customer_id, customer_name, email, total_orders, total_spent) VALUES (%s, %s, %s, %s, %s)",
            tuple(row)
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted successfully!")

if __name__ == "__main__":
    create_tables()
    load_data()
