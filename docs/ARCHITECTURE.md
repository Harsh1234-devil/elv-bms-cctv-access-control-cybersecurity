# ELV / BMS / CCTV / Access Control Cybersecurity Architecture

## 1. Reference Environment

This project models a modern enterprise facility/data-center environment where IT infrastructure, building systems and physical-security systems are interconnected.

## 2. High-Level Architecture

```text
                           INTERNET
                              |
                       EDGE FIREWALL
                              |
                         DMZ / VPN
                              |
                  +-----------+-----------+
                  |                       |
             ENTERPRISE IT          VENDOR ACCESS
                  |                       |
             CORE NETWORK           JUMP SERVER / PAM
                  |
        +---------+---------+
        |         |         |
       BMS       CCTV      ACS
        |         |         |
      HVAC       VMS    Controllers
        |         |         |
    Sensors    Cameras   Door Readers
        |
    UPS / Power
        |
   Facility Systems
