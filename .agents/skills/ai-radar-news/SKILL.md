---
name: ai-radar-news
description: Find recent AI news, assess it as source-backed AI Radar signals, and save a dated daily JSON file using the repository contract. Use when the user asks for AI news or asks to turn AI news into AI Radar signals.
metadata:
  short-description: Turn recent AI news into daily AI Radar signals
---

# AI Radar News

When the user asks for recent AI news, find and present five important, current items as AI Radar signals. Respond in the user's language. Unless they request another period or count, use the latest relevant news and five signals.

## Workflow

1. Browse the web for current AI news. Prefer primary announcements for product claims and reputable reporting for independent context. Check publication dates and distinguish reported facts from company claims or analysis.
2. Select five distinct items for practical significance to builders, considering capability and product changes, research, security, policy, infrastructure, and market impact. Avoid filling the list with repeated coverage of one event.
3. For each item, capture a descriptive title, source name and direct URL, publication date, concise evidence, likely impact, a practical next action, and an explicit status. Do not present an inference as confirmed fact.
4. Inspect the repository before writing. Use its existing daily signal schema if present; if no contract exists, create a JSON Schema contract under `contracts/` and make the daily data conform to it. Preserve existing files and adapt to existing conventions.
5. Save the daily result as `data/daily/YYYY-MM-DD.json`, using the current local date unless the user specifies another date. Keep source links and dates in the file so each signal is traceable.
6. Present the signals in chat with citations, then report the contract and daily JSON paths. Do not claim validation unless a validator was actually run.

## Signal contract

Use the existing contract as authoritative. For this repository's initial contract, the daily object contains `date`, `product`, and `signals`; each signal has `id`, `title`, `source` (`name`, `url`, `published_at`), `evidence`, `impact`, `action`, and `status`. Status values must follow the schema. Keep evidence concise and source-grounded. Use a status that describes the news lifecycle (such as announced, launched, published, or reported); use verification-pending only when a material claim still needs independent confirmation.

## Quality and scope

- Use direct links to the publisher, original announcement, study, or other evidence where possible.
- Attribute self-reported benchmarks and financial figures; state when independent confirmation is unavailable.
- Keep recommendations actionable and proportionate; do not give investment advice based on a news item.
- Do not overwrite `AGENTS.md` or unrelated repository files as part of this workflow.
- If browsing is unavailable, say so and do not invent current news or fabricate a daily snapshot.
