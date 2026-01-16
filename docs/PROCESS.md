# Process

## Purpose

This document describes how the system evolves safely and how changes are classified and reviewed. The system evolves by constitution, not by improvisation.

## Pull Request Structure

Each pull request must include:

- **Scope statement:** what is being changed and why it is within scope.
- **Classification:** documentation-only, implementation, or constitutional.
- **Constitution check:** confirmation that the change aligns with constitutional rules.
- **Traceability:** links to the relevant documents or sprint scope.

Pull requests must be explicit and auditable. Unscoped changes are not valid.

## Relationship to Sprints

Sprints define the allowed scope of work. A pull request must map to a sprint or be rejected. If a change does not align with an active sprint, it must not proceed.

## Change Classification

### Documentation-Only

- Documentation files only.
- No changes to runtime behavior, architecture, protocols, metrics, or agents.

### Implementation

- Changes to code or execution behavior.
- Must remain within constitutional bounds and sprint scope.

### Constitutional

- Changes to the Constitution or its formal annexes.
- Must follow the amendment policy defined in the governance documents.

## Constitutional Change Procedure

Constitutional changes are proposed through a dedicated amendment process. They must be explicit, justified within governance rules, and reviewed for systemic coherence and traceability before adoption.

## Governance Emphasis

All evolution must remain consistent with constitutional authority. Changes are validated through audit and traceability, not through informal decisions.
