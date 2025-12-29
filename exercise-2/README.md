# Exercise 2 – CI/CD Pipeline Design

## Overview
This exercise demonstrates the design of a CI/CD pipeline for a Python-based web application deployed to Kubernetes. The focus is on showing a clear and reliable delivery flow rather than executing a live deployment.

## Pipeline Flow
The pipeline is triggered when code is pushed to the main branch. It begins by building a Docker image for the application, followed by running automated tests to validate functionality. A security scanning stage is included to identify vulnerabilities early in the process.

## Environment Promotion
After validation, the application is automatically deployed to the staging environment. This allows testing in an environment that closely resembles production. Promotion to production is intentionally gated with a manual approval step to reduce deployment risk.

## Rollback Strategy
In case of issues after deployment, rollback is handled by redeploying a previously known stable container image. This approach allows fast recovery without rebuilding artifacts.

## Secret and Credential Management
Secrets such as cloud credentials, Kubernetes access details, and API keys are never stored in the repository. Instead, they are managed using GitHub Secrets and injected into the pipeline securely at runtime. In a production setup, this strategy can be extended using cloud-native secret managers like AWS Secrets Manager or HashiCorp Vault for better rotation and auditing.

## Assumptions
This exercise focuses on pipeline design and documentation. The pipeline demonstrates structure, security awareness, and deployment flow rather than a fully operational system.
