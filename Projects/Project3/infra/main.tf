# Bucket to store website
resource "google_storage_bucket" "website" {
  name = "my-unique-bkt-name"
  location = "US"
}

# Upload index.html (object) to the bucket
resource "google_storage_bucket_object" "website_src" {
  name = "index.html"
  source = "../website/index.html"
  bucket = google_storage_bucket.website.name
}

# Make the object publicly accesible
resource "google_storage_object_access_control" "public_rule" {
  
}
