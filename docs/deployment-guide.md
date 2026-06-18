# Deployment Guide

## Overview

This project uses GitHub Actions to deploy a FastAPI-based MCP Authorization Server to Azure App Service.

---

# Deployment Architecture

Developer
↓
GitHub Repository
↓
GitHub Actions
↓
Azure App Service
↓
Production Deployment

---

# Azure Resources

## Resource Group

```text
rg-agentic-ai-platform
```

## App Service

```text
app-mcp-agentic-security-prod
```

## Application Insights

```text
app-mcp-agentic-security-prod
```

---

# Deployment Pipeline

Workflow file:

```text
.github/workflows/main_app-mcp-agentic-security-prod.yml
```

Pipeline stages:

1. Checkout Code
2. Build Application
3. Install Dependencies
4. Package Application
5. Deploy to Azure App Service
6. Restart Application

---

# Runtime Configuration

Environment Variables

```text
TENANT_ID
API_AUDIENCE
TOOL_REGISTRY_STORAGE_ACCOUNT
TOOL_REGISTRY_CONTAINER
TOOL_REGISTRY_FILE
```

---

# Verification

## Health Check

```http
GET /health
```

## Tool Discovery

```http
GET /tools
```

## Authorization

```http
POST /authorize-tool
```

---

# Common Issues Resolved

## Deployment Conflict

HTTP 409

Resolution:

Re-run GitHub workflow.

---

## Dependency Failure

ModuleNotFoundError

Resolution:

Validate requirements.txt.

---

## Python Runtime Error

IndentationError

Resolution:

Correct source code and redeploy.

---

# Operational Status

Deployment successful.

Production service operational.
