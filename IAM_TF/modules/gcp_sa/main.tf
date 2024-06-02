locals {
  names = toset(var.names)
}

resource "google_service_account" "service_account" {
  for_each = local.names
  account_id = each.value
  display_name = var.display_name # "TF-Managed SA"
  description = var.description # "Created via TF"
  project = var.project_id
}

resource "google_project_iam_member" "iam_member" {
  for_each = local.names
  project = var.project_id
  role = var.role
  member = "serviceAccount:${google_service_account.service_account[each.value].email}"
  condition {
    expression = var.condition.expression
    title = var.condition.title
  }
}
