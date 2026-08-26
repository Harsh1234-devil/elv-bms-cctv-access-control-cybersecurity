# VULN-001 — Vendor VPN Authentication Weakness

## Finding Information

| Field | Value |
|---|---|
| Finding ID | VULN-001 |
| Asset ID | ELV-013 |
| Asset | Vendor VPN Gateway |
| Security Domain | Remote / Vendor Access |
| Severity | Critical |
| Risk Score | 95/100 |
| CVSS-Style Score | 9.1 |
| ATT&CK | T1078 — Valid Accounts |
| Status | Open |

---

## 1. Observation

The simulated vendor VPN gateway permits remote access to the facility environment using vendor accounts.

The assessment identified insufficient authentication assurance for privileged remote connectivity.

The primary concern is that compromise of a vendor identity could provide an attacker with an initial foothold into the internal environment.

---

## 2. Attack Scenario

```text
Compromised Vendor Credentials
             |
             v
        Vendor VPN
             |
             v
       Internal Access
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
   Critical Facility Impact
