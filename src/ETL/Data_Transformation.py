import pandas as pd

# Function to clean product data
def clean_product_data(df):
    df.dropna(inplace=True)
    df['price'] = df['price'].astype(float)
    df['category'] = df['category'].str.strip().str.title()
    return df

# Function to clean customer data
def clean_customer_data(df):
    df.dropna(inplace=True)
    df['email'] = df['email'].str.lower()
    df['city'] = df['city'].str.strip().str.title()
    return df

# Function to clean order data
def clean_order_data(df):
    df.dropna(inplace=True)
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df

if __name__ == "__main__":
    # Load raw data
    products_df = pd.read_csv("data/processed_data/products.csv")
    customers_df = pd.read_csv("data/processed_data/customers.csv")
    orders_df = pd.read_csv("data/processed_data/orders.csv")

    # Clean data
    products_df = clean_product_data(products_df)
    customers_df = clean_customer_data(customers_df)
    orders_df = clean_order_data(orders_df)

    # Save cleaned data
    products_df.to_csv("data/cleaned_data/cleaned_products.csv", index=False)
    customers_df.to_csv("data/cleaned_data/cleaned_customers.csv", index=False)
    orders_df.to_csv("data/cleaned_data/cleaned_orders.csv", index=False)
