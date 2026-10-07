---
inclusion: fileMatch
fileMatchPattern: 'docs/About/release-notes*'
---

# Writing Spira Release Notes

Current file: `docs/About/release-notes-v9.md` (one file per major version).

## Structure

Newest version first. Patch releases (`9.5.0.1`) get their own `##` section above the
minor release they patch.

```markdown
## Version 9.5 (September 2026)
!!! info "Summary"
    One or two sentences on the release theme. Link to new docs pages.

??? success "New Features"
    - Feature description [RQ:6510]

??? bug "Bug fixes and enhancements"
    - Item [IN:12784]
```

- Admonition content is indented 4 spaces.
- Every item ends with one or more ticket refs: `[IN:12345]`.
- Patch releases usually have only a `??? bug` section, no summary.
- Most entries need no prose description — the title and the page it links to carry it.
- If a description genuinely adds something, keep it to one or two sentences (~40 words): what users can now do, and why it matters. Then stop. Do not enumerate capabilities, caveats, or permission and read-only behavior; the linked manual page covers those.

## Ordering inside "Bug fixes and enhancements"

One flat list, sorted alphabetically (case-insensitive) by item text. No sub-grouping —
enhancements, grouped lines, and bug fixes all sort together. In practice this puts
`Add...` / `Allow...` first, then the `Fix...` block, then `Improve...`, `Rename...`,
`Security fixes`, `Update...`, `Upgrade...`.

- Ignore markdown link syntax when sorting; sort on the visible text.
  `Fix [exploratory test execution page](...)` sorts under "e".
- Ignore the trailing `[IN:xxxxx]` refs.
- Grouped lines take their alphabetical position like any other item.

## Grouping

Collapse these into a single line with multiple ticket refs:

- `Documentation and Knowledge Base article updates and enhancements [IN:xxxx] [IN:yyyy]`
- `Inflectra-Spira MCP Server improvements and fixes [IN:xxxx] [IN:yyyy]`
- `Security fixes [IN:xxxx] [IN:yyyy]`
- `Performance enhancements for database query [IN:xxxx] [IN:yyyy]`

## Exclude entirely

- Anything tagged `Internal-Process`.
- Internal infrastructure: developer sandbox CDK configs, internal repo `.gitignore` changes,
  CloudManager debug options.
- Research spikes and investigation tickets.

## Wording

Keep bug descriptions generic — no reproduction steps that would help someone exploit the
issue on an older version. Avoid specific column names, API endpoint paths, and internal
error messages.

- Bad: "Fix false notifications when reordering cards in the same column on incident boards"
- Good: "Fix a bug where false notifications could be sent when reordering cards on planning boards"

For AI model changes, stay generic: "Upgrade Inflectra.ai to use newer AI models" — don't name
specific models.

## New feature vs. enhancement

A New Feature must give users a capability they didn't have. Changes that serve Inflectra
rather than the user (e.g. the login page marketing banner, IN:12621) are enhancements.
