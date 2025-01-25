from google.cloud import bigquery
import pandas as pd

# Set up BigQuery client
def create_bigquery_client():
    client = bigquery.Client()
    return client

# Function to upload a DataFrame to BigQuery
def upload_to_bigquery(df, dataset_id, table_id):
    client = create_bigquery_client()
    table_ref = client.dataset(dataset_id).table(table_id)
    job_config = bigquery.LoadJobConfig(
        schema=[bigquery.SchemaField(name, "STRING") for name in df.columns],
        write_disposition="WRITE_TRUNCATE",  # Overwrite the table
    )
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()  # Wait for the job to complete
    print(f"Loaded {job.output_rows} rows to {dataset_id}.{table_id}")

# Function to query BigQuery
def query_bigquery(query):
    client = create_bigquery_client()
    query_job = client.query(query)
    return query_job.result()  # Returns rows as a list of dictionaries

# Example usage
if __name__ == "__main__":
    # Load the example data
    products_df = pd.read_csv("example_products.csv")
    customers_df = pd.read_csv("example_customers.csv")

    # Upload data to BigQuery
    upload_to_bigquery(products_df, 'your_dataset_id', 'products_table')
    upload_to_bigquery(customers_df, 'your_dataset_id', 'customers_table')

    # Run a query
    query = "SELECT * FROM `your_project_id.your_dataset_id.products_table`"
    products_results = query_bigquery(query)
    print("Products Table:")
    for row in products_results:
        print(row)

    query = "SELECT * FROM `your_project_id.your_dataset_id.customers_table`"
    customers_results = query_bigquery(query)
    print("\nCustomers Table:")
    for row in customers_results:
        print(row)

