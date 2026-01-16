# Review Signals

This document describes how reviewers should interpret governance signals in documentation and pull requests. It focuses on interpretation rather than enforcement.

## Signals Reviewers Should Look For

### Presence of Non-Goals

- Non-goals are explicitly stated.
- Non-goals match the sprint or document scope.
- The absence of non-goals is treated as a governance risk.

### Explicit Scope Boundaries

- Scope is described in bounded, neutral language.
- Scope does not expand beyond documented protocol and Constitution.
- Scope statements avoid prescriptive or outcome-oriented language.

### Sprint Alignment

- Work references the current sprint goal.
- Deliverables match the sprint work items.
- Deviations are documented as non-goals or exclusions.

### Constitutional References

- Changes remain consistent with the Constitution.
- Documentation defers to the Constitution as the source of truth.
- Any ambiguity is treated as unresolved governance work.

### Absence of Prescriptive Language

- Documentation avoids recommendations and evaluations.
- Language describes structure, boundaries, and traceability.
- Outcome claims are treated as governance smells.

## Healthy PR Indicators

- Clear scope, goal, and non-goals.
- Documentation-only changes when required by the sprint.
- Explicit references to relevant governance documents.
- No implied behavioral changes.

## Governance Smells

- Missing non-goals or unclear scope.
- Claims about effectiveness, quality, or outcomes.
- Protocol or behavior changes without governed justification.
- Ambiguous alignment with the Constitution.

## Silence and Ambiguity

Silence or ambiguity is treated as a failure signal because it prevents reviewers from validating governance alignment. If a document does not state scope, non-goals, and alignment, reviewers cannot determine whether the work is governed.
