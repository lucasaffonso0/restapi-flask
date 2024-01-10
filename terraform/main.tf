module "kubernetes" {
  source       = "git@github.com:lucasaffonso0/restapi-flask.git?ref=flask-api"
  cidr_block   = "10.0.0.0/16"
  project_name = "restapi"
  region       = "us-west-2"
  tags = {
    Department = "DevOps"
  }
}