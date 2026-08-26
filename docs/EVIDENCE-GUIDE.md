# Evidence Collection & Assessment Artifacts

## Purpose

This document defines the evidence structure used to support cybersecurity assessment findings across ELV, BMS, CCTV, Access Control and critical facility infrastructure.

All evidence in this repository is simulated or sanitized for educational and portfolio purposes.

---

## 1. Evidence Principles

Assessment evidence should be:

- Authorized
- Relevant
- Repeatable
- Traceable
- Time-stamped
- Non-destructive
- Sanitized
- Linked to a specific finding

Never publish:

- Real credentials
- Passwords
- API keys
- Production IP addresses
- Customer information
- Sensitive network diagrams
- Security-camera recordings
- Access-control credentials
- Confidential configuration data

---

## 2. Evidence Directory

Recommended structure:

```text
evidence/
├── architecture/
├── asset-inventory/
├── network/
├── authentication/
├── bms/
├── cctv/
├── access-control/
├── remote-access/
├── vulnerability-scans/
├── screenshots/
└── findings/
