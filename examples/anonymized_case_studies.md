# Anonymized Empirical Case Studies (Pre-Bid Auditing)

## Case Study 1: Proprietary API Lock-In vs. Open REST API Equivalence
* **Initial Restrictive Clause:** Mandated direct native integration with a proprietary legacy subsystem, locking out independent vendors without closed partner-tier SDK access.
* **Audit Engine Detection:** Flagged under `EU-2014-24-ART42-LOCKIN-API` (Art. 42 of Directive 2014/24/EU).
* **Official Outcome:** The contracting authority formally amended the tender terms, confirming that standard open REST API integration meets the functional specification.

## Case Study 2: COTS Licensing vs. Full Source-Code Transfer Contradiction
* **Initial Restrictive Clause:** Functional specification allowed mature COTS platforms, while the draft contract required full source code handover into the buyer internal GitLab repository and exclusive IP transfer.
* **Audit Engine Detection:** Flagged under `EU-2014-24-CROSS-COTS-SOURCE` (Cross-document contradiction between Technical Annex and Draft Contract IP clauses).
* **Official Outcome:** The contracting authority revised the draft contract IP provisions to separate background software licensing from bespoke custom development deliverables.

## Case Study 3: Deprecated Vendor Certifications & SLA Consistency
* **Initial Restrictive Clause:** Qualification gates demanded discontinued vendor certificates alongside conflicting SLA response hours across annexes.
* **Audit Engine Detection:** Flagged under `EU-2014-24-ART58-DEPRECATED-CERT`.
* **Official Outcome:** The contracting authority updated the qualification table to accept active equivalent certifications and harmonized SLA timeframes.