# Rust Engineering Learning Path

> A production-oriented Rust learning handbook for an experienced programmer.
>
> **Baseline:** Rust 1.98.0 (released 2026-08-20) · **Edition:** Rust 2024 · **Status:** Stable-first

## What this repository is

This is a structured path from Rust fundamentals to advanced systems engineering. It is designed to teach not only syntax, but the mental model behind Rust: ownership, borrowing, lifetimes, algebraic data types, traits, zero-cost abstractions, concurrency, async execution, unsafe boundaries, FFI, performance, testing, and production tooling.

The goal is **competence**, not merely finishing tutorials. Every section therefore follows this pattern:

1. Learn the model.
2. Read a small example.
3. Modify it.
4. Solve exercises without looking at the solution.
5. Build something real.
6. Review the code with `cargo fmt`, `cargo clippy`, tests, and documentation.

## Official baseline

The handbook's **baseline** is Rust **1.98.0** (August 20, 2026), and its material uses the **2024 Edition** idioms. The current stable toolchain moves every six weeks (Rust 1.100.0 shipped 2026-11-12), so treat the baseline as the minimum supported version and update this note when your toolchain moves materially forward. [Rust 1.98.0 release](https://blog.rust-lang.org/2026/08/20/Rust-1.98.0/) · [The Rust Programming Language](https://doc.rust-lang.org/book/) · [Rust Editions](https://doc.rust-lang.org/stable/book/appendix-05-editions.html)

## Roadmap

| Stage | Focus | Outcome |
|---|---|---|
| 0 | Toolchain and Cargo | Create, build, test, format, lint, document, publish crates |
| 1 | Language fundamentals | Write idiomatic basic Rust without fighting the compiler |
| 2 | Ownership and borrowing | Understand why Rust code is safe and how data moves through a program |
| 3 | Types and abstraction | Use enums, pattern matching, generics, traits, iterators, closures |
| 4 | Project architecture | Organize crates/modules, errors, tests, docs, configuration |
| 5 | Concurrency | Use threads, channels, `Send`, `Sync`, locks, atomics safely |
| 6 | Async Rust | Understand futures, executors, tasks, cancellation, I/O, backpressure |
| 7 | Advanced Rust | Lifetimes in depth, trait objects, associated types, macros, pinning |
| 8 | Unsafe and systems | Raw pointers, FFI, invariants, unsafe abstractions, ABI boundaries |
| 9 | Performance | Allocation, cache behavior, profiling, benchmarking, zero-copy design |
| 10 | Production | Observability, CI, security, dependency hygiene, releases, cross-platform builds |

## Suggested study order

Read the files in this order:

- `01-fundamentals.md`
- `02-ownership-borrowing-lifetimes.md`
- `03-types-traits-generics.md`
- `04-projects-testing-errors.md`
- `05-concurrency-async.md`
- `06-advanced-unsafe-ffi-performance.md`
- `07-production-projects-reference.md`

Do not jump into `unsafe`, async, or advanced lifetime tricks before ownership and borrowing are comfortable.

### Single-file edition

`RUST-LEARNING-HANDBOOK-2026.md` is a generated, self-contained copy of this README plus all seven chapters
plus `RUST-STUDY-TRACKER.md`. **Edit the chapter files, never the composite.** Rebuild it with:

```bash
python build-handbook.py           # regenerate the composite
python build-handbook.py --check   # verify it is current (used in CI)
```

## Environment setup

Install Rust with `rustup`, the official recommended toolchain manager:

```bash
# Unix-like systems / WSL
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Verify
rustc --version
cargo --version
rustup show
```

On Windows, use the official `rustup-init.exe` installer. Windows builds may require the MSVC C++ build tools. See the official installation guide: https://rust-lang.org/tools/install/

### Create a Rust 2024 project

```bash
cargo new rust-playground
cd rust-playground
cargo run
```

A modern `Cargo.toml` should explicitly identify the edition when you want predictable project configuration:

```toml
[package]
name = "rust-playground"
version = "0.1.0"
edition = "2024"

[dependencies]
```

### Core commands

```bash
cargo check                 # fast type checking
cargo build                 # debug build
cargo build --release       # optimized build
cargo run                   # run binary
cargo test                  # run tests
cargo fmt                   # format code
cargo fmt -- --check        # verify formatting
cargo clippy                # lint
cargo doc --open            # generate/open docs
cargo tree                  # inspect dependencies
cargo update                # update dependency resolution
cargo clean                 # remove build artifacts
```

Clippy is a collection of lints for correctness, suspicious code, style, complexity, and performance. Prefer treating warnings as useful review signals rather than suppressing them blindly. https://doc.rust-lang.org/stable/clippy/

## Engineering rules used throughout this handbook

- Prefer safe Rust. Reach for `unsafe` only when a measurable requirement or foreign/system boundary justifies it.
- Prefer explicit error handling in library code. Avoid `unwrap()` and `expect()` on paths where failure is expected or externally controlled.
- Keep ownership decisions local and obvious.
- Avoid unnecessary cloning. First understand why a value cannot be borrowed or moved as intended.
- Prefer strong types over stringly-typed state.
- Keep public APIs small and documented.
- Test behavior, edge cases, failure paths, and invariants—not merely line coverage.
- Benchmark before optimizing.
- Treat dependency selection as an engineering decision: license, maintenance, security, compile-time cost, and API stability all matter.
- Use `cargo fmt`, `cargo clippy`, and `cargo test` as normal development steps.

## Learning checkpoints

You are ready to move forward when you can explain the previous stage **without quoting the compiler error back to yourself**.

### Checkpoint: ownership

You should be able to explain:

- why a move can invalidate the source binding;
- when `Copy` applies;
- why `&T` and `&mut T` are different contracts;
- why a reference cannot outlive the value it points to;
- why two mutable aliases are rejected;
- why cloning is sometimes the wrong fix.

### Checkpoint: abstractions

You should be able to design a small library using enums, traits, generics, iterators, and error types without relying on dynamic typing.

### Checkpoint: concurrency

You should be able to explain `Send`, `Sync`, ownership across threads, shared state, channels, and why Rust rejects a data race at compile time in safe code.

### Checkpoint: async

You should be able to explain the difference between an async function, a future, a task, and an executor—and identify blocking work that should not run inside an async task.

## Canonical official references

1. [The Rust Programming Language (The Book)](https://doc.rust-lang.org/book/)
2. [The Rust Reference](https://doc.rust-lang.org/stable/reference/)
3. [The Cargo Book](https://doc.rust-lang.org/cargo/)
4. [Rust By Example](https://doc.rust-lang.org/rust-by-example/)
5. [Rust Standard Library](https://doc.rust-lang.org/std/)
6. [Rust Edition Guide](https://doc.rust-lang.org/edition-guide/)
7. [The Async Book](https://rust-lang.github.io/async-book/)
8. [The Rustonomicon](https://doc.rust-lang.org/nomicon/)
9. [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
10. [Rust Reference: FFI](https://doc.rust-lang.org/reference/items/external-blocks.html)

## Important source notes

The Rust Book is the primary guided learning resource. The Reference is more detailed and comprehensive for language semantics. The Rustonomicon is specifically for advanced unsafe Rust and assumes considerable Rust/system-programming knowledge. The Async Book covers async concepts and the ecosystem but explicitly notes that it is undergoing a rewrite; use it as a companion rather than the only async authority.

## How to use this offline

Open these Markdown files in any editor, GitHub, VS Code, Obsidian, Typora, or a Markdown reader. Code blocks are deliberately plain Markdown so the handbook remains portable.

## Completion standard

Do not define “finished Rust” as memorizing the language. A better standard is:

> I can read unfamiliar idiomatic Rust, explain its ownership and type behavior, design a safe API, diagnose compiler errors, write tests, reason about concurrency, and choose when advanced or unsafe techniques are actually justified.
