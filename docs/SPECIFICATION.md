# Specification

## Purpose

This specification converts the Constitution into an operational, developer-facing contract for documentation, implementation, and review. It is descriptive and normative, and it does not introduce new metrics or behavior.

## Core Units

### Task

A Task is a defined objective with explicit constraints and explicit context.

- **Objective:** what is being requested or processed.
- **Constraints:** formal limits that must be respected (data rules, separation rules, governance rules).
- **Context:** the data and scope that allow the Task to be interpreted without inference.

A Task must be traceable to a source and must not imply decisions beyond the provided scope.

### Action

An Action is a derived, operational step that executes a Task within defined constraints.

- It is **derived** from a Task and does not introduce independent intent.
- It is **operational** and follows declared procedures.
- It is **non-decisional** and does not alter governance rules, protocols, or metrics.

Actions are valid only when they preserve the epistemic separation defined by the Constitution.

### Report

A Report is a descriptive output that is audited and traceable.

- It must be reproducible from its inputs.
- It must preserve historical, analytical, and simulation boundaries.
- It must be attributable to a Task and a sequence of Actions.

**Forbidden in a Report:**

- prescriptive directives
- judgments
- performance-improvement claims
- subjective language

A Report is invalid if any forbidden content appears.

## Neutral Execution

Neutral execution means the system performs defined operations without adding evaluation, preference, or prescriptive content. Outputs are limited to factual description, formal analysis, or controlled simulation, and must remain within the declared scope of the Task.

## Audit Outcomes

Audits verify structural, analytical, cognitive, semantic, and governance conformity. An audit has two outcomes:

- **Approved:** the artifact is fully conformant and traceable.
- **Rejected:** any nonconformity invalidates the artifact and requires correction before reuse.

## Separation Requirements

The system enforces strict separation:

- **Historical** data is observed and never hypothetical.
- **Simulation** is hypothetical and never historical evidence.
- **Visualization** presents data without altering historical or simulation content.

Historical ≠ Simulation ≠ Visualization.

## Governance Priority

When there is conflict, the Constitution governs all subordinate documentation and implementation. No document may override constitutional definitions or permissions.
