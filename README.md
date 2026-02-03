# Python DevSecOps Project

A Python application with DevSecOps practices, deployed using Helm and ArgoCD, with monitoring via Prometheus and Grafana.

## Features

- Python application with secure coding practices
- Continuous deployment using **ArgoCD**
- Deployment packaged with **Helm**
- Monitoring using **Prometheus** and **Grafana**

## Architecture

Python App -> Docker -> Helm Chart -> ArgoCD -> Kubernetes
|
v
Prometheus & Grafana Monitoring


## Prerequisites

- Kubernetes cluster (minikube, EKS, GKE, etc.)
- Helm >= 3.x
- ArgoCD installed
- Prometheus & Grafana installed in the cluster
- kubectl configured
