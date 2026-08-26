# Threat Model & Attack Paths

## 1. Threat Modeling Objective

This project identifies realistic cyber-physical attack scenarios affecting ELV, BMS, CCTV, Access Control and critical facility infrastructure.

The assessment focuses on initial access, privilege escalation, lateral movement, impact and recovery.

## 2. Threat Actors

| Threat Actor | Capability | Objective |
|---|---|---|
| External Attacker | Medium-High | Gain unauthorized access |
| Ransomware Operator | High | Disrupt critical operations |
| Malicious Insider | Medium | Abuse legitimate access |
| Compromised Vendor | Medium-High | Abuse trusted remote access |
| Opportunistic Attacker | Low-Medium | Exploit exposed systems |

## 3. Attack Surface

Primary attack surfaces include:

- Vendor VPN
- Remote administration
- BMS interfaces
- CCTV VMS
- Access Control servers
- Engineering workstations
- Network management interfaces
- IoT and field devices
- Weak authentication
- Insecure protocols
- Poor network segmentation
- Backup infrastructure

## 4. Attack Path A — Vendor VPN to BMS

```text
External Attacker
      |
      v
Vendor VPN Gateway
      |
      v
Vendor Account
      |
      v
PAM / Jump Server
      |
      v
BMS Server
      |
      v
HVAC Controller
      |
      v
Critical Facility Impact
