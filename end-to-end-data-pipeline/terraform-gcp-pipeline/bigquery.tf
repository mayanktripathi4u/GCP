resource "google_bigquery_dataset" "customer_dataset" {
  dataset_id = "customer_data"
  project    = var.project-id
}

resource "google_bigquery_table" "customer_table" {
  dataset_id = google_bigquery_dataset.customer_dataset.dataset_id
  table_id   = "customers"
  schema     = file("schemas/customer_schema.json")
  project    = var.project-id
}