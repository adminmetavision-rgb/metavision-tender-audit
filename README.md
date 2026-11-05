# MetaVision Tender Audit

**Open-Source EU Public Procurement Lock-In & Compliance Analyzer**
*License: Apache 2.0 | Local-First (Ollama / vLLM / OpenAI-compatible REST API)*

**MetaVision Tender Audit** is an open-source, privacy-preserving procurement intelligence and specification auditing engine. It ingests EU Tenders Electronic Daily (TED) eForms (`XML`/`JSON`) and national tender packages (`PDF`/`DOCX`) to perform automated technical-legal cross-examination against **EU Directive 2014/24/EU** principles.

* **Interactive Prototype Node:** [https://tenders.metavision.click](https://tenders.metavision.click)
* **Project Portal:** [https://metavision.click](https://metavision.click)

## Core Architecture (Neuro-Symbolic Pipeline)
1. **Multi-Document Graph Parser:** Maps annexes, qualification gates, SLA tables, and IP clauses across fragmented PDF/DOCX/XML packages.
2. **Symbolic Rule Engine:** Deterministic regex and taxonomy checks for missing *"or equivalent"* clauses (Art. 42), deprecated certifications (Art. 58), and CPV/SLA anomalies.
3. **Local LLM Auditor (Ollama / vLLM):** Cross-document semantic contradiction detection and multilingual terminology mapping without exposing commercial strategies to external cloud providers.
4. **Automated Pre-Bid Inquiry Generator:** Produces structured, legally cited clarification requests ready for submission during Market Consultations (PIN) or active open procedures.

## Quick Start (Local CLI Prototype)
```bash
git clone [https://github.com/adminmetavision-rgb/metavision-tender-audit.git](https://github.com/adminmetavision-rgb/metavision-tender-audit.git)
cd metavision-tender-audit
python3 src/audit_engine.py --input examples/sample_spec.txt --skip-llm
```

## Development Roadmap
* **Milestone 1:** Multi-Format Ingestion Engine & EU TED / Document Graph Parser
* **Milestone 2:** Hybrid Lock-In & Compliance Rule Engine
* **Milestone 3:** Automated Pre-Bid Inquiry Generator & Local Web UI Integration
* **Milestone 4:** Multilingual Validation, Documentation & Packaging