# Repository conventions

This is a Markdown documentation repository. There is no Rust code to compile here —
every `rust` fence is illustrative teaching material. Do not attempt to `cargo build` the repo.

## Source of truth

The chapter files are authoritative:

- `README.md` — the front page, roadmap, and study order
- `01-fundamentals.md` … `07-production-projects-reference.md` — the chapters
- `RUST-STUDY-TRACKER.md` — the progress checklist

`RUST-LEARNING-HANDBOOK-2026.md` is **generated**. Never edit it by hand.

## Editing workflow

1. Edit the relevant chapter file.
2. Regenerate the composite: `python build-handbook.py`
3. Verify: `python build-handbook.py --check` (must print `ok`).

CI runs the check and fails if the composite drifts from its parts.

## Content rules

- Target **Rust 2024 Edition** idioms. When a 2024 rule differs from older material, say so.
- Version facts: 1.98.0 is the stated **baseline**, not "the current release". Do not restate the
  baseline as current; check `https://blog.rust-lang.org/releases/` when touching version claims.
- Every `rust` code block must compile in the context it is presented (or be explicitly marked `// invalid`).
  Snippets that are statements only should rely on the chapter's "assume inside `fn main()`" note.
- Prefer linking the canonical docs: Nomicon at `doc.rust-lang.org/nomicon/` (not `/stable/nomicon/`).
- Link checks: run any Markdown link checker before release if one is available.

## Style

- One `#` heading per file (the chapter title), `##` for sections, `###` for subsections.
- Fenced blocks always carry a language tag (`rust`, `bash`, `toml`, `text`).
- Reference URLs are plain, full, and verifiable — no shortened or invented paths.
