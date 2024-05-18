
resource "google_storage_bucket" "dataflow_bucket" {
  name     = "end-to-end-data-pipeline-prj"
  location = "US"
  project  = var.project-id
}

