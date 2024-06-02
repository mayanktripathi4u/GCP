variable "rolesList" {
  type = list(string)
  default = [ "roles/storage.admin", "roles/pubsub.admin" ]
}

variable "project_id" {
  type = string
  default = "my-project-1234"
}