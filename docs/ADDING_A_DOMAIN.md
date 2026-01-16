# Adding a New Domain (Governed Checklist)

## Purpose

This checklist defines the required, governed artifacts for adding a new domain while preserving protocol and constitutional constraints.

## Required Artifacts

- Domain documentation that identifies scope, labels, and data field mapping.
- Historical, simulation, and visualization documentation that preserves epistemic separation.
- Audit and traceability notes connecting domain artifacts to the protocol.

## Naming and Folder Rules

- Applications must be placed under the `applications/` directory.
- Domain folders must use explicit, stable naming.
- Documentation files must live under `docs/` and be linked in `docs/README.md`.

## Separation Rules (Historical vs Simulation vs Visualization)

- Historical data remains observed and non-hypothetical.
- Simulation data remains hypothetical and non-historical.
- Visualization remains a presentation layer and does not modify data.

## Protocol Mapping (Task / Action / Report)

- Tasks must be expressed with objective, constraints, and context.
- Actions must be derived from Tasks and remain non-decisional.
- Reports must be descriptive, auditable, and traceable.

## Documentation Requirements Before Code Acceptance

- Domain documentation and mapping artifacts are required before code review.
- Protocol mapping must be declared and traceable to the Constitution.
- Separation rules must be stated explicitly in domain documentation.

## Explicit Non-Goals

- No new metrics or analytical definitions.
- No changes to protocol semantics.
- No new outputs or runtime behavior.
