resource "google_service_account" "tf_sa" {
  account_id = "terraform-user"
  display_name = "Terraform User"
}

resource "google_project_iam_binding" "tf_sa" {
  project = var.project_id
  count = length(var.rolesList)
  role = var.rolesList[count.index]
  members = [
    "serviceAccount: ${google_service_account.tf_sa.email}"
  ]
}