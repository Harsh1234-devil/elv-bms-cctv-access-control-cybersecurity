# VULN-001 — Remediation & Re-Test Summary

## Finding

**Finding ID:** VULN-001  
**Asset:** Vendor VPN Gateway  
**Severity:** Critical  
**Original Risk Score:** 95/100  
**Status:** Remediated — Pending Re-Test

---

## 1. Remediation Actions

The following security controls were implemented in the simulated environment:

| Control | Before | After |
|---|---|---|
| MFA | Not consistently enforced | Mandatory |
| Vendor Access | Persistent | Time-bound |
| Privileged Access | Partial PAM | PAM enforced |
| Session Recording | Disabled | Enabled |
| Network Access | Broad access | Restricted |
| SIEM Monitoring | Partial | Centralized |
| Vendor Accounts | Persistent | Lifecycle controlled |

---

## 2. Target Architecture

```text
Vendor
   |
   v
MFA
   |
   v
Vendor VPN
   |
   v
PAM / Jump Server
   |
   v
Restricted Management Zone
   |
   +------ BMS
   +------ CCTV
   +------ ACS
   |
   v
SIEM Monitoring
