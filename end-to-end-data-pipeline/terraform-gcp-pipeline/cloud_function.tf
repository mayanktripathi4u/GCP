# Generates an archive of the source code compressed as a .zip file.
data "archive_file" "source" {
  type        = "zip"
  source_dir  = "./functions"
  output_path = "${path.module}/function.zip"
}
# path.module is the filesystem path of the module where the expression is placed. 
# We do not recommend using path.module in write operations because it can produce different behavior depending on whether you use remote or local module sources.

# Add source code zip to the Cloud Function's bucket (Cloud_function_bucket) 
resource "google_storage_bucket_object" "zip" {
  source       = data.archive_file.source.output_path
  content_type = "application/zip"
  name         = "src-${data.archive_file.source.output_md5}.zip"
  bucket       = google_storage_bucket.dataflow_bucket.name
  depends_on = [
    google_storage_bucket.dataflow_bucket,
    data.archive_file.source
  ]
}

resource "google_cloudfunctions_function" "generate_synthetic_data" {
  name                  = "generateSyntheticData"
  runtime               = "python310"
  project               = var.project-id
  region                = var.region
  entry_point           = "generate_data"
  source_archive_bucket = google_storage_bucket.dataflow_bucket.name
  source_archive_object = google_storage_bucket_object.zip.name
  trigger_http          = true

  environment_variables = {
    PUBSUB_TOPIC = google_pubsub_topic.customer_topic.name
  }
}