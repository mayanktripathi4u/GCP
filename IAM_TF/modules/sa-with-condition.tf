module "sa-with-condition" {
  source = "./modules/gcp-service-account"
  project_id = "my-project-id-12345"
  names = ["sa-ima-condition-tf"]
  role = "roles/compute.instanceAdmin"
  condition = {
    # all time should be in UTC.
    expression = "request.time < timestamp(\"2024-05-22T10:55:33.866Z\")"
    title = "expire-20-mins"
  }
}