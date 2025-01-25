
import pandas as pd
import json
from sqlalchemy import create_engine

# Define database connection strings
db_config = {
    'mysql': 'mysql+pymysql://username:password@localhost:3306/ecommerce',
    'postgresql': 'postgresql+psycopg2://username:password@localhost:5432/ecommerce',
    'mongodb': 'mongodb://localhost:27017/ecommerce'
}

# Extract data from multiple sources
def extract_from_mysql():
    engine = create_engine(db_config['mysql'])
    query = "SELECT * FROM orders"
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)
    return df

def extract_from_postgresql():
    engine = create_engine(db_config['postgresql'])
    query = "SELECT * FROM customers"
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)
    return df

def extract_from_mongodb():
    from pymongo import MongoClient
    client = MongoClient(db_config['mongodb'])
    db = client['ecommerce']
    collection = db['products']
    data = list(collection.find({}, {"_id": 0}))
    df = pd.DataFrame(data)
    return df

# Transform data
def transform_data(df):
    df.dropna(inplace=True)
    return df

# Load data into a centralized location
def load_to_csv(df, file_path):
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    # Extract data
    orders_df = extract_from_mysql()
    customers_df = extract_from_postgresql()
    products_df = extract_from_mongodb()

    # Transform data
    orders_df = transform_data(orders_df)
    customers_df = transform_data(customers_df)
    products_df = transform_data(products_df)

    # Load data into CSV files
    load_to_csv(orders_df, "data/processed_data/orders.csv")
    load_to_csv(customers_df, "data/processed_data/customers.csv")
    load_to_csv(products_df, "data/processed_data/products.csv")
