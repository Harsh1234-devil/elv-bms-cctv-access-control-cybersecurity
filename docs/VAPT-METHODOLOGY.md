# ELV / BMS / CCTV / Access Control VAPT Methodology

## 1. Purpose

This methodology defines a controlled approach for assessing the cybersecurity posture of ELV, BMS, CCTV, Access Control and supporting facility infrastructure.

The methodology is designed to identify vulnerabilities while minimizing the risk of operational disruption to critical facility systems.

> All examples in this project use simulated infrastructure and synthetic assessment data.

---

## 2. Assessment Objectives

The assessment aims to:

- Identify exposed assets and services
- Validate security architecture
- Evaluate network segmentation
- Assess authentication and authorization
- Identify vulnerable software and devices
- Evaluate remote/vendor access
- Assess management interfaces
- Identify attack paths
- Validate security controls
- Prioritize remediation

---

## 3. Rules of Engagement

Before testing begins:

1. Define assessment scope.
2. Identify authorized assets.
3. Identify critical systems.
4. Establish testing windows.
5. Define prohibited activities.
6. Confirm emergency contacts.
7. Establish rollback procedures.
8. Obtain formal authorization.

### Prohibited Activities

The following should not be performed against production facility systems without explicit authorization:

- Denial-of-service testing
- Destructive exploitation
- Uncontrolled malware execution
- Firmware modification
- Physical bypass testing
- Unapproved credential attacks
- Safety-system manipulation

---

# 4. Assessment Phases

## Phase 1 — Planning & Scoping

### Activities

- Define objectives
- Identify stakeholders
- Establish scope
- Document system dependencies
- Identify critical services
- Establish rules of engagement

### Deliverables

- Scope document
- Asset list
- Testing plan
- Communication plan

---

## Phase 2 — Asset Discovery

Identify:

- Servers
- Workstations
- Network devices
- BMS controllers
- HVAC systems
- CCTV cameras
- VMS servers
- Access controllers
- Readers
- VPN gateways
- PAM systems
- UPS interfaces
- Monitoring systems

### Discovery Data

Capture:

- Asset ID
- Hostname
- IP address
- System type
- Security domain
- Zone
- Criticality
- Owner
- Exposure

---

## Phase 3 — Architecture Review

Review:

- Network topology
- Security zones
- Firewall placement
- VLANs
- Routing
- Remote access
- Management networks
- BMS/OT connectivity
- CCTV segmentation
- Access Control segmentation

### Key Question

> Can compromise of one system provide unintended access to another security domain?

---

## Phase 4 — Service & Configuration Assessment

Assess:

- Open ports
- Network services
- Administrative interfaces
- Authentication mechanisms
- Encryption
- Default credentials
- Password policies
- Configuration weaknesses
- Insecure protocols
- Firmware versions
- Patch status

---

## Phase 5 — Vulnerability Assessment

### Technical Checks

- Known vulnerabilities
- Unsupported software
- Weak configurations
- Exposed services
- Credential weaknesses
- Missing patches
- Insecure protocols
- Excessive privileges
- Missing security controls

### Evidence

Every finding should contain:

- Finding ID
- Affected asset
- Evidence
- Risk description
- Severity
- Likelihood
- Business impact
- Recommendation

---

# 5. Controlled Penetration Testing

Penetration testing should validate whether identified weaknesses can realistically be chained into an attack path.

## Example

```text
Vendor VPN
     |
     v
Compromised Account
     |
     v
PAM / Jump Server
     |
     v
BMS Network
     |
     v
BMS Server
     |
     v
HVAC Controller
     |
     v
Facility Impact
