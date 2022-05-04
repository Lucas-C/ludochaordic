Title: Deploying AWS API Gateway static endpoints using Terraform
Date: 2022-05-04 20:00
Tags: lang:en, oui.sncf, http, aws, api, api-gateway, openapi, swagger, terraform, kiss-principle, auth, iac, prog
---
Recently at work, at [SNCF Connect & Tech](https://jobs.connect-tech.sncf),
we needed to expose some static documents as HTTP endpoints:
a `GET /version` that would provide some information about the application version as JSON,
and a `GET /openapi/yaml` that would return the [OpenAPI 3 specification](https://swagger.io/specification/) of our HTTP API as YAML.

We thought about several solutions, like deploying a lambda or exposing data from a S3 bucket using API Gateway,
but given our needs and our existing technical stack, the cheapest & simplest solution ([KISS](https://en.wikipedia.org/wiki/KISS_principle))
was to use [API Gateway Mock integrations](https://docs.amazonaws.cn/en_us/apigateway/latest/developerguide/how-to-mock-integration.html).

![Terraform and API Gateway logos](images/2022/05/terraform-plus-api-gateway.png)

As I haven't found much documentation about that while I was setting up those endpoints, especially to do so using [Terraform](https://www.terraform.io/),I thought it may be useful to share some code snippets in this article.

Our application is deployed using Terraform, which configure AWS API Gateway endpoints
[using an OpenAPI specification](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.html). I won't get into the details on how to set up and configure those tools,
and directly jump straight to [HCL code](https://github.com/hashicorp/hcl#hcl):

```terraform
locals {
  open_api_spec = {
    openapi : "3.0.1"
    info : {
      title   : "My pretty API"
      version : "1.0"
    }
    paths : {
      "/version" : {
        get : {
          responses : {
            200 : {
              description : "200 response"
            }
          }
          # Doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration.html
          x-amazon-apigateway-integration : {
            type : "mock"
            requestTemplates : {
              "application/json" : jsonencode({
                statusCode : 200
              })
            }
            responses : {
              default : {
                statusCode : 200
                responseTemplates : {
                  "application/json" : jsonencode({
                    "app_name"             : var.app_name
                    "aws_region"           : var.aws_region
                    "environment"          : var.environment
                    "git_branch"           : var.git_branch
                    "git_ref"              : var.git_ref
                    "last_deployment_time" : timestamp()
                    "terraform_workspace"  : terraform.workspace
                    "app_version"          : var.app_version
                  })
                }
              }
            }
          }
        }
      }
      "/openapi/yaml" : {
        get : {
          responses : {
            200 : {
              description : "200 response",
              headers : {
                Content-Type : {
                  type : "string"
                }
              }
            }
          }
          # Doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration.html
          x-amazon-apigateway-integration : {
            type : "mock"
            requestTemplates : {
              "application/json" : jsonencode({
                statusCode : 200
              })
            }
            responses : {
              default : {
                statusCode : 200
                responseTemplates : {
                  "application/yaml" : file("path/to/openapi.yaml")
                }
                responseParameters : {
                  "method.response.header.Content-Type" : "'application/yaml'"  # default is application/json
                },
              }
            }
          }
        }
      }
    }
    x-amazon-apigateway-request-validators : {
      all : {
        validateRequestBody : true,
        validateRequestParameters : true
      }
    }
  }
}

resource "aws_api_gateway_rest_api" "api" {
  name                     = var.api_name
  body                     = jsonencode(local.open_api_spec)
  endpoint_configuration {
    types            = ["PRIVATE"]
    vpc_endpoint_ids = [var.vpce_id]
  }
}
```

This makes use of the [`aws` provider for Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_rest_api).I did not provide a full working example, an choose to instead only focus on the parts relevant to the subject.
Note also that the above configuration does not include any authentication method, so the endpoints will be public.

The beauty of this approach is that a few lines of [Infrastructure As Code (IAC)](https://en.wikipedia.org/wiki/Infrastructure_as_code)
quickly gets you an exposed endpoint, with no need to store JSON/YAML files on any file repository.
The endpoints content will get updated each time you perform a new `terraform apply`,
and that's it. I guess a [Swagger UI HTML page](https://swagger.io/tools/swagger-ui/) could even be served using the same approach.

Finally, this recipe could probably be improved by inserting parts of the `openapi.yaml` spec file
into the `open_api_spec` Terraform local value, to avoid duplicating some information.

I hope those code snippets will help some fellow developers.
Have fun building HTTP APIs! 🏗️ ☁
