# What is Terraform?

- Terraform is a tool that facilitates "Infrastructure as Code" (aka "IaC")

# How do I use Terraform?

- terraform code (stored in files that end in `.tf`) is declarative code for the infrastructure you want
- `terraform` the command line tool is how you deploy that code, which creates the infrastructure you want
- Working from "fine" Grain to "coarse" Grain:
  - `resource`:
    - resources are the "atom"/finest Grain unit of terraform - a resource block defines an individual infrastructure object.
      - The following defines an AWS RedShift cluster ([documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/redshift_cluster))
        ```terraform
        resource "aws_redshift_cluster" "example" {
          cluster_identifier = "tf-redshift-cluster"
          database_name      = "mydb"
          master_username    = "exampleuser"
          master_password    = "Mustbe8characters"
          node_type          = "dc1.large"
          cluster_type       = "single-node"
        }
        ```
      - You can have one or multiple `resource` blocks in one `.tf` file.
  - `variable`:
    - Input variables are analogous to function arguments in a general purpose programming language. These variables are used as inputs to `resource`s:
      ```terraform
      variable "serverless_base_capacity" {} 
      variable "serverless_max_capacity" {} 
      resource "aws_redshiftserverless_workgroup" "analytics_wg" {
        base_capacity = var.serverless_base_capacity
        max_capacity = var.serverless_max_capacity
        # ...other arguments...
      }
      ```
  - `module`:
    - A module is a collection of `resource`s that are grouped together. There are 2 main subdivisions of modules:
      - 1. The Root Module
        - The Root module is at least one, but possibly multiple `.tf` files in the same working directory.
          - This can go by other names such as a "configuration" or "group" (Concert naming convention).
      - 2. Reusable Module
        - re-usable modules are also groups `resources`. However, creating 
        - re-usable modules can be thought off as terraform's version of a function.
  - `output`:
    - Output values are an analogous to return values in general purpose programming languages.
    - The main use case of an `output` is when you are developing a Reusable Module; you would declare an `output` in the Reusable Module code, and then when you call that Reusable Module (as a Child Module (terraform lingo)), you can reference that output in other parts of your Root Module/configuration.
