import psycopg2
import pandas as pd

def load_data():
    conn = psycopg2.connect("dbname=ecommerce user=admin password=pass host=localhost")
    cursor = conn.cursor()
    df = pd.read_csv("data/transformed_data.csv")

    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO orders (order_id, product, price, date, customer_id) VALUES (%s, %s, %s, %s, %s)",
            (row["order_id"], row["product"], row["price"], row["date"], row["customer_id"])
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Data Loaded to PostgreSQL")
