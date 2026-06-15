# Agents

Reusable briefs for the specialized sub-agents that do the company's legwork. Each brief is a prompt/spec that can be handed to a Claude sub-agent. Outputs are written into the matching [`research/`](../research/) folder.

| Agent | Brief | Output lands in |
|---|---|---|
| Niche Research | [`niche-research/BRIEF.md`](niche-research/BRIEF.md) | `research/niches/` |
| Supplier Sourcing | [`supplier-sourcing/BRIEF.md`](supplier-sourcing/BRIEF.md) | `research/dropship-availability/` |
| Marketing | [`marketing/BRIEF.md`](marketing/BRIEF.md) | `research/marketing/` |
| Storefront | [`storefront/BRIEF.md`](storefront/BRIEF.md) | `storefront/` |

## Conventions

- Each agent run produces a dated, sourced markdown file. Cite links for every claim.
- Use the selection scorecard in [`docs/strategy.md`](../docs/strategy.md).
- Flag any spend before it happens — nothing is bought without a line in `finance/budget.md`.
