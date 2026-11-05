#!/usr/bin/env python3
"""MetaVision Tender Audit - Core Neuro-Symbolic Auditing Prototype (CLI)"""
import argparse, json
from pathlib import Path

def load_rules(rules_path: Path):
    return json.loads(rules_path.read_text(encoding="utf-8"))

def run_symbolic_checks(text: str, rules_data: dict):
    findings, lower_text = [], text.lower()
    for rule in rules_data.get("rules", []):
        matched = [p for p in rule.get("patterns", []) if p.lower() in lower_text]
        cc = rule.get("cross_check", {})
        if cc:
            s_hits = [s for s in cc.get("spec_indicators", []) if s.lower() in lower_text]
            c_hits = [c for c in cc.get("contract_indicators", []) if c.lower() in lower_text]
            if s_hits and c_hits:
                matched.extend(s_hits + c_hits)
        if matched:
            findings.append({
                "rule_id": rule["rule_id"],
                "category": rule["category"],
                "directive_article": rule["directive_article"],
                "severity": rule["severity"],
                "matched_indicators": matched,
                "suggested_inquiry": rule["remediation_template"]
            })
    return findings

def main():
    parser = argparse.ArgumentParser(description="MetaVision Tender Audit CLI")
    parser.add_argument("--input", required=True)
    parser.add_argument("--rules", default="rules/eu_directive_2014_24_rules.json")
    parser.add_argument("--skip-llm", action="store_true")
    args = parser.parse_args()
    spec_text = Path(args.input).read_text(encoding="utf-8")
    rules_data = load_rules(Path(args.rules))
    findings = run_symbolic_checks(spec_text, rules_data)
    print(json.dumps({"engine": "MetaVision Tender Audit v0.1.0", "findings": findings}, indent=2))

if __name__ == "__main__":
    main()