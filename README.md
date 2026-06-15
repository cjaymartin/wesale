# wesale

A drop-ship business, built and operated as a small autonomous company. Claude acts as CEO; specialized sub-agents handle research, sourcing, marketing, and storefront build-out.

## Mission

Find a profitable drop-ship niche, source reliable suppliers, stand up a storefront, and reach profitability as fast as possible on a **total budget of $500**.

## Operating principles

1. **Profit fast, spend slow.** Every dollar is tracked in [`finance/`](finance/). Validate demand before paying for inventory commitments or premium tooling.
2. **Research before commitment.** No niche is chosen, and no money is spent, until the research folders justify it.
3. **One source of truth.** Decisions and their rationale live in [`docs/`](docs/). Raw findings live in [`research/`](research/).
4. **Agents do the legwork.** Reusable agent briefs live in [`agents/`](agents/); their outputs land in [`research/`](research/).

## Structure

| Folder | Purpose |
|---|---|
| [`agents/`](agents/) | Briefs / prompts for the specialized sub-agents (niche research, supplier sourcing, marketing, storefront). |
| [`research/`](research/) | Findings: candidate niches, dropship/supplier availability, marketing channels, competitor analysis. |
| [`storefront/`](storefront/) | Storefront build-out — platform choice, theme, product pages, eventually code. |
| [`marketing/`](marketing/) | Channel plans, ad creative, content calendar, launch playbook. |
| [`finance/`](finance/) | Budget ledger ($500 cap), unit economics, P&L. |
| [`docs/`](docs/) | Strategy, decisions (ADRs), and the running playbook. |

## Status

- **Phase:** 0 — Research & niche selection
- **Budget remaining:** $500.00 / $500.00 (see [`finance/budget.md`](finance/budget.md))
- **Niche:** Not yet selected

## Roadmap

- [ ] **Phase 0 — Research:** niche candidates, supplier availability, channel feasibility, competitor scan.
- [ ] **Phase 1 — Selection:** pick 1 niche + 2–3 hero products with a defensible margin and a clear traffic path.
- [ ] **Phase 2 — Build:** stand up storefront, list hero products, set up payments + tracking.
- [ ] **Phase 3 — Launch:** small paid test + organic, measure CAC vs. margin.
- [ ] **Phase 4 — Scale or pivot:** double down on winners, kill losers.
