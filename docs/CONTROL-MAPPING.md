# Security Control Mapping

## Purpose

This document maps the identified ELV, BMS, CCTV, Access Control and critical-facility risks to recognized cybersecurity controls and MITRE ATT&CK techniques.

The mapping supports security architecture review, remediation planning and control validation.

---

## 1. NIST CSF 2.0 Mapping

| Finding | NIST CSF Function | Category / Focus | Security Objective |
|---|---|---|---|
| VULN-001 | Protect | Identity Management, Authentication & Access Control | Strengthen vendor authentication |
| VULN-002 | Protect | Identity Management, Authentication & Access Control | Secure privileged access |
| VULN-003 | Protect | Platform Security | Segment BMS infrastructure |
| VULN-004 | Protect | Platform Security | Harden CCTV infrastructure |
| VULN-005 | Protect | Identity Management | Secure access-control authentication |
| VULN-006 | Detect | Continuous Monitoring | Improve facility-system visibility |
| VULN-007 | Protect | Platform Security | Maintain secure device configuration |
| VULN-008 | Recover | Incident Recovery | Strengthen backup and recovery |
| VULN-009 | Protect | Network Security | Secure network administration |
| VULN-010 | Protect | Platform Security | Protect UPS management |
| VULN-011 | Protect | Identity Management | Reduce administrative exposure |
| VULN-012 | Protect | Endpoint Security | Secure facilities administration endpoints |

---

## 2. MITRE ATT&CK Mapping

| Finding | ATT&CK Technique | Technique Name | Security Relevance |
|---|---|---|---|
| VULN-001 | T1078 | Valid Accounts | Compromised vendor credentials may enable unauthorized access |
| VULN-002 | T1078 | Valid Accounts | Privileged credentials can be abused |
| VULN-003 | T1021 | Remote Services | Remote access can enable lateral movement |
| VULN-004 | T1046 | Network Service Scanning | Exposed services may support reconnaissance |
| VULN-005 | T1078 | Valid Accounts | Weak local credentials increase compromise risk |
| VULN-006 | T1562 | Impair Defenses | Limited monitoring can reduce detection capability |
| VULN-007 | T1587 | Develop Capabilities | Vulnerable devices may become attack targets |
| VULN-008 | T1490 | Inhibit System Recovery | Backup weaknesses can increase ransomware impact |
| VULN-009 | T1021 | Remote Services | Network management services may support lateral movement |
| VULN-010 | T1078 | Valid Accounts | Local credentials may be abused |
| VULN-011 | T1078 | Valid Accounts | Administrative endpoints can become privileged access paths |
| VULN-012 | T1021 | Remote Services | Compromised administration endpoints may enable movement |

---

## 3. IEC 62443 Security Concepts

The assessment also considers IEC 62443-style security concepts relevant to operational and facility systems.

| Security Principle | Application |
|---|---|
| Zones and Conduits | Separate BMS, CCTV, ACS and management networks |
| Least Privilege | Restrict administrative and vendor access |
| Defense in Depth | Combine segmentation, authentication, monitoring and endpoint controls |
| Secure Remote Access | Control and monitor vendor connectivity |
| System Integrity | Maintain secure configurations and firmware |
| Availability | Protect critical facility systems from disruption |
| Security Monitoring | Detect anomalous activity across cyber-physical systems |

---

## 4. ISO/IEC 27001 Security Themes

| Security Theme | Project Application |
|---|---|
| Access Control | MFA, PAM and least privilege |
| Asset Management | Centralized ELV/BMS/CCTV/ACS inventory |
| Operations Security | Secure configuration and monitoring |
| Communications Security | Network segmentation and protected management channels |
| Supplier Security | Vendor remote-access controls |
| Incident Management | Cyber-physical attack response |
| Business Continuity | Backup, recovery and resilience |

---

## 5. Control Priorities

### Priority 1 — Identity & Access

- MFA
- PAM
- Least privilege
- Vendor session controls
- Centralized authentication

### Priority 2 — Network Segmentation

- Dedicated BMS/OT zone
- Dedicated CCTV zone
- Dedicated Access Control zone
- Restricted management VLANs
- Firewall ACLs

### Priority 3 — Monitoring

- SIEM integration
- Centralized logging
- Endpoint monitoring
- Network telemetry
- Privileged session monitoring

### Priority 4 — Resilience

- Secure configuration backups
- Offline/isolated backups
- Recovery testing
- Redundant critical systems

---

## 6. Control Validation

Security controls should be validated through:

1. Architecture review
2. Configuration review
3. Vulnerability assessment
4. Controlled penetration testing
5. Log verification
6. Access-control testing
7. Segmentation testing
8. Backup restoration testing
9. Incident-response exercises
10. Periodic reassessment

---

## 7. Target Security Architecture

```text
                 INTERNET
                     |
               EDGE FIREWALL
                     |
                  DMZ/VPN
                     |
              +------+------+
              |             |
          Vendor VPN     Enterprise IT
              |             |
             PAM       Management Zone
              |             |
              +------+------+
                     |
               Security Firewall
                     |
      +--------------+--------------+
      |              |              |
     BMS            CCTV            ACS
      |              |              |
     HVAC           VMS         Controllers
      |              |              |
   Sensors        Cameras       Door Readers
      |
 UPS / Facilities

              ↓
       Central Monitoring
              ↓
             SIEM
