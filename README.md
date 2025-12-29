# DevOps Exercise 1 – Infrastructure as Code

## Overview
This project demonstrates a simple Infrastructure as Code (IaC) approach using Terraform to provision cloud resources on AWS. The goal is to show how infrastructure can be defined, versioned, and managed through code instead of manual configuration.

## Architecture Description
The design includes a Virtual Private Cloud (VPC) to provide network isolation and an S3 bucket to store static assets. In a real production environment, this setup would be extended to include load balancers, application servers, and a database inside private subnets.

## Security Considerations
The VPC provides network-level isolation. Sensitive components such as databases would be placed in private subnets and accessed only through controlled security group rules. No secrets are hardcoded in the Terraform files.

## Environment Configuration
All configurations are parameterized using variables so the same code can be reused across development, staging, and production environments.

## Assumptions
- This exercise focuses on design and structure rather than full deployment
- Resources are defined at a high level for clarity
- AWS is used as the cloud provider, but the design can be adapted to others
## Architecture Description (Textual Diagram)

The infrastructure is designed following a simple and secure layered architecture.

Users access the application through the internet, which is fronted by an Application Load Balancer. The load balancer resides in a public subnet inside a Virtual Private Cloud (VPC) and distributes incoming traffic to application servers running in private subnets.

The application servers are part of an Auto Scaling Group, allowing the system to scale based on demand while maintaining availability across multiple availability zones.

A relational database (RDS) is deployed in private subnets and is only accessible by the application servers, ensuring that sensitive data is never exposed to the public internet.

An S3 bucket is used to store static assets such as images or files. All networking components are isolated within the VPC and protected using security groups that follow the principle of least privilege.
