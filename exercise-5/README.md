# Exercise 5 – Kubernetes Deployment

## Overview
This exercise demonstrates a multi-tier Kubernetes application consisting of a frontend (nginx), backend API, and Redis cache. The focus is on resource management, observability, scalability, and self-healing behavior.

## Resource Management
Each deployment defines CPU and memory requests and limits to ensure predictable scheduling and prevent resource contention within the cluster.

## Scaling and Self-Healing
Horizontal Pod Autoscaling is configured for the backend service based on CPU utilization. Kubernetes automatically restarts unhealthy pods using liveness probes and removes unready pods from traffic using readiness probes.

## Configuration and Secrets
Application configuration is managed using ConfigMaps, while sensitive values such as credentials are stored in Kubernetes Secrets to avoid hardcoding sensitive data.

## Security
Network policies restrict backend access so that only the frontend can communicate with it. This limits blast radius and follows the principle of least privilege.

## Deployment Instructions
These manifests can be applied to a local Kubernetes cluster using tools like minikube or kind with standard kubectl apply commands.
