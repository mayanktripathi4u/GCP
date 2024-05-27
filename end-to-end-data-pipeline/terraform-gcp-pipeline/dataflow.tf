
resource "google_dataflow_job" "dataflow_to_bq" {
  name = "dataflow-job"
  # template_gcs_path = "gs://dataflow-templates/latest/PubSub_to_BigQuery"
  template_gcs_path = "gs://dataflow-templates-us-east4/latest/PubSub_to_BigQuery"
  temp_gcs_location = "gs://mt_devops_bkt_01/tmp/"
  project           = var.project-id
  region            = var.region

  parameters = {
    inputTopic  = google_pubsub_topic.customer_topic.id
    outputTableSpec = "${google_bigquery_dataset.customer_dataset.dataset_id}.${google_bigquery_table.customer_table.table_id}"
  }
}

