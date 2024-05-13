from google.cloud import bigquery

def create_dataset(dataset_id):
    # Initialize BigQuery client
    client = bigquery.Client()

    # Construct dataset reference object
    dataset_ref = client.dataset(dataset_id)

    # Construct dataset object
    dataset = bigquery.Dataset(dataset_ref)

    # Create the dataset
    dataset = client.create_dataset(dataset)  # API request

    print(f"Dataset {dataset.dataset_id} created.")

def create_table(dataset_id, table_id, schema):
    # Initialize BigQuery client
    client = bigquery.Client()

    # Construct dataset reference object
    dataset_ref = client.dataset(dataset_id)

    # Construct table reference object
    table_ref = dataset_ref.table(table_id)

    # Construct table object
    table = bigquery.Table(table_ref, schema=schema)

    # Create the table
    table = client.create_table(table)  # API request

    print(f"Table {table.table_id} created.")

# Example usage
if __name__ == "__main__":
    dataset_id = "streamingDataSet"
    table_id = "customers"
    schema = [
        bigquery.SchemaField("customer_name", "STRING"),
        bigquery.SchemaField("address", "STRING"),
        bigquery.SchemaField("dob", "STRING"),
        bigquery.SchemaField("email", "STRING"),
        bigquery.SchemaField("purchase_date", "STRING"),
        bigquery.SchemaField("purchase_amount", "STRING"),
        bigquery.SchemaField("purchased_product", "STRING"),
        bigquery.SchemaField("order_id", "STRING"),
        # bigquery.SchemaField("address", "INTEGER"),
        # bigquery.SchemaField("column3", "FLOAT"),
        # Add more schema fields as needed
    ]

    create_dataset(dataset_id)
    create_table(dataset_id, table_id, schema)
