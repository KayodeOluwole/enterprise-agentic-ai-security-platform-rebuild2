# Enterprise MCP Authorization Server - Agentic AI Security Platform

## Project Overview

This project implements a production-oriented MCP (Model Context Protocol) Authorization Server designed to secure Agentic AI environments through identity-based access control, tool authorization, approval workflows, audit logging, and enterprise deployment practices.

The objective was to build practical expertise in Agentic AI Security Architecture, MCP Security, Agent Authorization, Tool Abuse Prevention, and Enterprise AI Governance using Microsoft Azure, Microsoft Entra ID, GitHub Actions, and Azure App Service.

---

# Business Problem

Modern AI agents can invoke tools, access enterprise systems, retrieve sensitive information, and perform actions autonomously.

Without proper controls, AI agents can:

* Execute unauthorized actions
* Access privileged tools
* Escalate privileges
* Abuse enterprise APIs
* Exfiltrate data
* Bypass governance controls

This project demonstrates how to implement enterprise-grade authorization controls before allowing AI agents to execute tools.

---

# Architecture

```text
Agent
  │
  ▼
MCP Authorization Server
  │
  ├── JWT Validation
  ├── Role-Based Access Control
  ├── Tool Registry
  ├── Risk Classification
  ├── Approval Workflow
  └── Audit Logging
        │
        ▼
Azure Monitoring
```

---

# Technology Stack

## Identity

* Microsoft Entra ID
* OAuth 2.0
* OpenID Connect
* JWT Validation
* App Roles

## Application

* Python 3.11
* FastAPI
* Uvicorn
* Gunicorn

## Cloud Platform

* Azure App Service
* Azure Application Insights
* Azure Storage Account

## DevSecOps

* GitHub
* GitHub Actions
* CI/CD Pipeline

## Monitoring

* Application Insights
* Azure Logs

---

# Security Capabilities

## Agent Identity

Implemented Microsoft Entra ID application registration to establish trusted agent identities.

### App Registration

```text
app-mcp-agentic-security-prod
```

### Controls

* Tenant restricted
* OAuth protected
* JWT token issuance
* Enterprise application registration

---

## Role Based Access Control (RBAC)

Implemented MCP-specific roles.

### Roles

```text
MCP.Platform.Admin
MCP.Tool.Operator
MCP.Tool.Reader
```

### Purpose

| Role               | Purpose                    |
| ------------------ | -------------------------- |
| MCP.Tool.Reader    | Discover and view tools    |
| MCP.Tool.Operator  | Execute approved tools     |
| MCP.Platform.Admin | Administrative tool access |

---

## Tool Registry

Implemented centralized tool inventory.

### Registered Tools

```json
{
  "tools": [
    {
      "name": "knowledge_search",
      "risk": "Low"
    },
    {
      "name": "incident_lookup",
      "risk": "Medium"
    },
    {
      "name": "send_notification",
      "risk": "High"
    },
    {
      "name": "admin_configuration",
      "risk": "Critical"
    }
  ]
}
```

---

## Risk Classification

Implemented risk-based authorization.

### Risk Levels

```text
Low
Medium
High
Critical
```

### Examples

| Tool                | Risk     |
| ------------------- | -------- |
| knowledge_search    | Low      |
| incident_lookup     | Medium   |
| send_notification   | High     |
| admin_configuration | Critical |

---

## Tool Authorization Engine

Implemented authorization decision engine.

### Authorization Logic

```text
Request Tool
      │
      ▼
Validate Tool
      │
      ▼
Validate JWT
      │
      ▼
Validate Role
      │
      ▼
Risk Evaluation
      │
      ▼
Allow / Deny
```

---

## Approval Workflow

Implemented approval requirement for privileged operations.

### Protected Operations

```text
High Risk
Critical Risk
```

Examples:

```text
send_notification
admin_configuration
```

---

## Audit Logging

Implemented authorization audit trail.

### Logged Events

```text
Tool Requested
Role Evaluated
Authorization Decision
Timestamp
Approval Requirement
```

### Event Type

```text
MCP_TOOL_AUTHORIZATION
```

---

# API Endpoints

## Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy",
  "service": "enterprise-mcp-authorization-server"
}
```

---

## Tool Discovery

```http
GET /tools
```

Returns registered tools and risk levels.

---

## Tool Authorization

```http
POST /authorize-tool
```

Example:

```json
{
  "tool_name": "admin_configuration"
}
```

---

# Security Testing Performed

## Health Validation

Validated application availability.

Result:

```text
PASS
```

---

## Tool Registry Validation

Validated tool inventory retrieval.

Result:

```text
PASS
```

---

## Request Validation

Tested invalid payload handling.

Result:

```text
422 Validation Error
PASS
```

---

## Unauthorized Access Test

Submitted request without valid role.

Response:

```json
{
  "authorized": false,
  "reason": "Missing required role: MCP.Platform.Admin"
}
```

Result:

```text
PASS
```

---

## Critical Tool Protection Test

Tested access to:

```text
admin_configuration
```

Result:

```text
Denied
PASS
```

---

## JWT Authorization Validation

Implemented:

* JWT extraction
* JWT validation
* Role extraction
* Audience validation
* Tenant validation

Result:

```text
PASS
```

---

# CI/CD Implementation

## Source Control

GitHub Repository

```text
enterprise-agentic-ai-security-platform-rebuild2
```

---

## Deployment Pipeline

```text
Developer
    │
    ▼
GitHub
    │
    ▼
GitHub Actions
    │
    ▼
Azure App Service
```

---

## Pipeline Activities

* Build
* Package
* Deploy
* Restart Application

---

# Production Issues Resolved

## Deployment Conflict

```text
HTTP 409
```

Resolved through deployment restart and workflow rerun.

---

## Application Stopped

```text
HTTP 403
Web App Stopped
```

Resolved by restarting App Service.

---

## Dependency Issues

```text
uvicorn not found
```

Resolved through requirements validation.

---

## Python Runtime Errors

```text
IndentationError
```

Resolved through code correction and redeployment.

---

# Lessons Learned

* Agent identity is foundational to Agentic AI security.
* Tool authorization must occur before tool execution.
* High-risk tools require approval workflows.
* JWT validation is critical for trust establishment.
* CI/CD pipelines are essential for enterprise deployment.
* Audit logging is mandatory for governance and compliance.
* MCP security extends traditional IAM into AI ecosystems.

---

# Project Outcomes

Successfully implemented:

* Agent Identity
* Agent Authentication
* Agent Authorization
* Agent RBAC
* MCP Security
* Tool Authorization
* Tool Abuse Prevention
* Approval Workflow
* Audit Logging
* GitHub CI/CD
* Azure Deployment
* Security Testing

---

# Future Enhancements

## Microsoft Sentinel Integration

Send authorization events to:

```text
Authorization Server
      │
      ▼
Log Analytics
      │
      ▼
Microsoft Sentinel
      │
      ▼
Analytics Rules
      │
      ▼
Incidents
```

## MITRE ATLAS Mapping

Map authorization events to:

* Tool Abuse
* Privilege Escalation
* Unauthorized Tool Execution
* Prompt Injection

## Automated Approval Workflow

Integrate:

* Logic Apps
* Service Bus
* Power Automate
* ServiceNow

---
CI/CD pipeline configuration stored in:

.github/workflows/main_app-mcp-agentic-security-prod.yml

# Author

Kayode Oluwole Isaiah, MSc, PMP, CISM, ITIL

Enterprise AI Security Architecture and Implementation Project

2026

