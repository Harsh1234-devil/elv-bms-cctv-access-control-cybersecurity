#!/usr/bin/env python3
"""
ELV / BMS / CCTV / Access Control Risk Engine

Reads the project vulnerability register and produces
a prioritized cybersecurity risk summary.

Dataset is synthetic and intended for portfolio/lab use.
"""

from __future__ import annotations

import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REGISTER = PROJECT_ROOT / "data" / "vulnerability-register.csv"


def risk_band(score: float) -> str:
    if score >= 90:
        return "CRITICAL"
    if score >= 75:
        return "HIGH"
    if score >= 50:
        return "MEDIUM"
    if score >= 25:
        return "LOW"
    return "INFORMATIONAL"


def load_findings(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Register not found: {path}")

    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    if not rows:
        raise ValueError("Vulnerability register is empty.")

    required = {
        "finding_id",
        "finding",
        "severity",
        "risk_score",
        "asset_name",
    }

    missing = required.difference(rows[0].keys())
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    return rows


def main() -> None:
    findings = load_findings(REGISTER)

    for row in findings:
        try:
            row["_risk"] = float(row["risk_score"])
        except ValueError as exc:
            raise ValueError(
                f"Invalid risk score for {row.get('finding_id', 'unknown')}"
            ) from exc

    findings.sort(key=lambda item: item["_risk"], reverse=True)

    average = sum(item["_risk"] for item in findings) / len(findings)
    highest = findings[0]

    counts = {}
    for row in findings:
        severity = row["severity"].upper()
        counts[severity] = counts.get(severity, 0) + 1

    print("=" * 60)
    print("ELV / BMS / CCTV CYBERSECURITY RISK ENGINE")
    print("=" * 60)
    print(f"Findings assessed : {len(findings)}")
    print(f"Average risk      : {average:.1f}/100")
    print(f"Overall rating    : {risk_band(average)}")
    print(
        f"Highest risk      : "
        f"{highest['finding_id']} - {highest['risk_score']}/100"
    )
    print()

    print("SEVERITY DISTRIBUTION")
    for severity in ("CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL"):
        print(f"{severity:15} {counts.get(severity, 0)}")

    print()
    print("TOP RISKS")
    print("-" * 60)

    for index, row in enumerate(findings[:8], start=1):
        print(
            f"{index:>2}. {row['finding_id']:<10} "
            f"{float(row['_risk']):>5.1f}  "
            f"{row['severity']:<9} "
            f"{row['asset_name']}"
        )


if __name__ == "__main__":
    main()
