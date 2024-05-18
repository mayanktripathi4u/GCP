
resource "google_cloud_scheduler_job" "call_function" {
  name      = "call-generate-synthetic-data"
  schedule  = "*/5 * * * *"
  time_zone = "Etc/UTC"

  http_target {
    http_method = "POST"
    uri         = google_cloudfunctions_function.generate_synthetic_data.https_trigger_url
  }
}
