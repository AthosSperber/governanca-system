# Constitutional Governance Process

## Amendment Proposal Workflow

1. **Create a PR** that includes the proposed change to the Constitution.
2. **Use a Conventional Commit** message scoped to `docs(constitution)` or `docs(governance)`.
3. **Include a rationale** explaining why the change is needed and what it enables or protects.
4. **Attach impact analysis** covering architecture, data lineage, reporting outputs, and auditability.
5. **Reference the amendment template** when applicable: `/templates/constitutional_amendment_pr.md`.

## Conflict Resolution (Priority Order)

When resolving conflicts, the system must follow this order of authority:

1. **Constitution**
2. **Business Rules**
3. **UX**
4. **Technical Implementation**

If a lower-priority artifact conflicts with the Constitution, it must be adjusted to comply.

## Breaking Constitutional Change

A change is **breaking** if it:

- Alters the constitutional scope or authority.
- Invalidates existing governance constraints.
- Requires changes to protocol semantics or audit guarantees.
- Modifies the separation between historical facts and hypotheses.

Breaking changes must be explicitly labeled in the PR and described in the changelog.

## Changelog Requirements

- Every amendment must update `/constitution/CHANGELOG.md`.
- The entry must include **date**, **version**, **summary**, and **impact**.
- Versions must progress as **v1.2, v1.3, ...** after v1.1.

## Required Rationale & Impact Analysis

Each constitutional change must document:

- The **reason** for the amendment.
- **Impact analysis** on architecture, reports, and audit processes.
- **Compatibility notes** for existing outputs and workflows.

