# Lessons Learned

## Technical Lessons

### MCP Security Requires Explicit Authorization

Tool discovery and tool execution should never be treated as the same operation.

Authorization must be enforced before execution.

---

### Risk-Based Tool Classification Is Essential

Not all tools should have equal permissions.

Implemented:

* Low
* Medium
* High
* Critical

risk categories.

---

### Deny-By-Default Improves Security

Access is denied unless the required role is present.

This significantly reduces the attack surface.

---

### JWT Validation Is Foundational

Agent identity must be verified before authorization decisions are made.

JWT validation provides:

* Identity verification
* Role extraction
* Trust establishment

---

### Audit Logging Is Required

Every authorization decision should be auditable.

Captured:

* Tool requested
* Role evaluated
* Authorization result
* Timestamp

---

## DevSecOps Lessons

### CI/CD Is Part Of Security

GitHub Actions enables:

* Change tracking
* Version control
* Deployment consistency
* Auditability

---

### Production Issues Are Valuable Learning Opportunities

Resolved:

* HTTP 409 deployment conflict
* Missing Python dependencies
* Azure deployment issues
* Runtime syntax errors
* API validation failures

These issues closely resemble real production incidents.

---

## Security Lessons

Enterprise Agentic AI security requires:

* Identity
* Authentication
* Authorization
* Tool governance
* Auditability
* Monitoring

All must work together.

---

# Project Outcome

Successfully built and deployed an Enterprise MCP Authorization Server using Azure, Microsoft Entra ID, GitHub Actions, FastAPI, and Application Insights.
