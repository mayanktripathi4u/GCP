1. Enable API's as below
    a. Cloud DNS API
    b. Compute Engine API
    c. IAM API

2. Create a Service Account for Terraform to authenticate to Google Cloud. Aas we are using TF to deploy our infrastructure for our website, it needs a way to authenticate to google cloud to deploy that infrastructure.

This need to be done manually from Console before starting with TF code.

Say SA as "terraform-gcp-sa", with Owner permission (set appropriate roles)

Get the API Key for the above SA. Generate in JSON format.

3. Start with Terraform Code
    1. provider.tf
    2. main.tf
    3. variables.tf

    
