# Domain Model

## Purpose

This document explains the domain model used in the system and clarifies that Academia is a reference domain, not the system itself. The protocol, governance, and epistemic separation are domain-independent.

## Why Academia is Used

Academia is chosen as a reference domain because it is simple, familiar, and bounded. This allows the model to be demonstrated without introducing domain-specific complexity.

## Generic Concepts

The system uses generic concepts that map to any domain:

- **Resource:** a bounded element with explicit capacity.
- **Activity:** a time-bound use of a resource.
- **Capacity:** a declared limit, never inferred.
- **Utilization:** observed use, treated as factual data.

These concepts are defined by the Constitution and remain stable across domains.

## What Changes in a New Domain

Adopting a new domain changes only the following:

- **Input data format:** fields and labels that represent the domain’s entities and events.
- **Labels:** human-facing naming for resources, activities, and sessions.
- **Visualization templates:** presentation structures tied to domain labels.

These changes are representational and do not alter the system’s protocol or governance.

## What Never Changes

The following are invariant across domains:

- **Protocol:** data contracts, validation rules, and formal definitions.
- **Governance rules:** constitutional constraints, audit requirements, and semantic restrictions.
- **Epistemic separation:** Historical ≠ Simulation ≠ Visualization.
