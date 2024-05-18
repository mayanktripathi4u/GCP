
# resource "google_pubsub_topic" "customer_topic" {
#   name = "customer-topic"
# }

resource "google_pubsub_topic" "customer_topic" {
  name    = "customer-topic"
  project = var.project-id
  labels = {
    foo = "end-to-end-project"
  }
  message_retention_duration = "86600s"
}