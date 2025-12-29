# Exercise 2 – CI/CD Pipeline Design

## Overview
This CI/CD pipeline is designed to automate the build, test, security scanning, and deployment of a Python web application to Kubernetes. The goal is to provide fast feedback to developers while ensuring quality and security before production releases.

## Pipeline Stages
The pipeline starts with building a Docker image after code is pushed to the main branch. Automated tests are executed next to validate application functionality. A security scanning stage follows to detect vulnerabilities early in the process.

## Deployment Strategy
After successful validation, the application is deployed automatically to the staging environment. Production deployment requires a manual approval step to reduce risk and ensure controlled releases.

## Rollback Strategy
If an issue is detected after deployment, rollback is handled by redeploying a previously known stable container image.

## Secret Management
Sensitive information such as credentials and API keys are not stored in the pipeline file. In a real environment, secrets would be managed using GitHub Secrets or a cloud-based secret manager and injected securely during runtime.
