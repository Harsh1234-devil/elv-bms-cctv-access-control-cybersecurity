# Security Findings & Risk Assessment

## Executive Summary

This assessment evaluates the simulated cybersecurity posture of an enterprise environment containing ELV, BMS, HVAC, CCTV, Access Control, management, networking and critical facility systems.

The analysis identified security weaknesses primarily involving remote access, privileged access, network segmentation, authentication, monitoring and recovery.

## Overall Risk

| Risk Area | Rating |
|---|---|
| Remote / Vendor Access | Critical |
| Privileged Access | High |
| BMS / OT Segmentation | Critical |
| CCTV Security | High |
| Access Control Security | High |
| Network Management | High |
| Facility / UPS Security | High |
| Monitoring & Logging | Medium |
| Backup & Recovery | High |

## Top Priority Findings

### VULN-001 — Vendor VPN Weak Authentication

**Asset:** Vendor VPN Gateway  
**Severity:** Critical  
**Risk Score:** 95/100  
**MITRE ATT&CK:** T1078 — Valid Accounts

#### Risk

Weak remote-access controls can allow a compromised vendor identity to become an entry point into the internal facility environment.

#### Potential Impact

- Unauthorized internal access
- Lateral movement
- BMS compromise
- Facility disruption

#### Recommendations

- Enforce MFA
- Apply conditional access
- Restrict vendor sessions by time
- Use PAM
- Record privileged sessions
- Monitor VPN activity

---

### VULN-003 — BMS Network Segmentation

**Asset:** BMS Application Server  
**Severity:** Critical  
**Risk Score:** 92/100  
**MITRE ATT&CK:** T1021 — Remote Services

#### Risk

Insufficient segmentation between BMS and enterprise networks can allow compromise of an IT system to spread into building-management infrastructure.

#### Potential Impact

- HVAC disruption
- Environmental control manipulation
- Facility availability impact
- Lateral movement

#### Recommendations

- Create a dedicated BMS security zone
- Deploy firewall ACLs
- Restrict management paths
- Implement jump-server access
- Monitor BMS traffic

---

### VULN-002 — Privileged Access Monitoring

**Asset:** PAM Jump Server  
**Severity:** High  
**Risk Score:** 84/100

#### Risk

Insufficient isolation and monitoring of privileged sessions can allow administrative credentials to be abused without timely detection.

#### Recommendations

- Enforce PAM
- Use MFA
- Record privileged sessions
- Apply just-in-time access
- Review privileged accounts regularly

---

### VULN-005 — Access Control Authentication

**Asset:** Door Controller 01  
**Severity:** High  
**Risk Score:** 82/100

#### Risk

Local administrative credentials increase the risk of unauthorized control of physical access systems.

#### Potential Impact

- Unauthorized entry
- Physical security bypass
- Increased cyber-physical exposure

#### Recommendations

- Centralize authentication
- Eliminate shared credentials
- Enforce strong authentication
- Segment access-control networks
- Monitor controller activity

---

### VULN-004 — CCTV Management Exposure

**Asset:** CCTV VMS Server  
**Severity:** High  
**Risk Score:** 78/100

#### Recommendations

- Isolate CCTV infrastructure
- Restrict management services
- Harden VMS configuration
- Patch firmware and software
- Monitor administrative activity

---

## Risk Prioritization

| Priority | Finding | Score | Severity |
|---|---|---:|---|
| 1 | Vendor VPN Authentication | 95 | Critical |
| 2 | BMS Segmentation | 92 | Critical |
| 3 | Privileged Access | 84 | High |
| 4 | Access Control Authentication | 82 | High |
| 5 | Backup / Recovery Controls | 80 | High |
| 6 | UPS Management Security | 79 | High |
| 7 | CCTV VMS Exposure | 78 | High |
| 8 | Network Management Security | 76 | High |

## Attack Path Risk

The highest-risk attack scenario is:

```text
Vendor VPN
     ↓
Vendor Account
     ↓
PAM / Jump Server
     ↓
BMS Server
     ↓
HVAC Controller
     ↓
Critical Facility Impact
