module "kubernetes" {
  source       = "/home/lucas/terraform-eks"
  cidr_block   = "10.0.0.0/16"
  project_name = "restapi"
  region       = "us-west-2"
  tags = {
    Department = "DevOps"
  }
}