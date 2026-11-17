# 07 — Production Rust, Projects, and Long-Term Reference

## 1. Production-readiness definition

A production Rust project is not merely code that compiles. It should have:

- reproducible builds;
- tests for critical behavior;
- formatting and linting;
- documented public APIs;
- meaningful errors;
- logging/observability;
- dependency review;
- CI checks;
- release/versioning policy;
- security response process;
- platform/build documentation.

## 2. CI baseline

A practical CI pipeline should at minimum execute:

```bash
cargo fmt -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo test --all-targets --all-features
cargo build --release
cargo doc --no-deps
```

Tune the exact flags to the project. Do not turn warnings into hard failures until the codebase is actually ready to maintain that contract.

## 3. Reproducibility

Commit the appropriate Cargo lockfile strategy for your project type and use CI/toolchain configuration consistently.

For applications, checking in `Cargo.lock` is normal. Library publishing has different considerations because downstream consumers resolve dependency versions within compatible constraints.

## 4. Toolchain management

`rustup` can manage stable, beta, nightly toolchains and additional targets. Prefer stable Rust for production unless a specific requirement makes an unstable feature necessary.

The official installation documentation recommends `rustup` for most developers: https://rust-lang.org/tools/install/

## 5. Stable vs nightly

A production decision should answer:

```text
Do we truly need the unstable feature?
Can stable Rust satisfy the requirement?
What is the maintenance cost of nightly?
What happens when the feature evolves?
```

Treat nightly dependencies as an explicit engineering trade-off.

## 6. Security posture

Rust's memory safety properties reduce a class of memory-safety bugs in safe code, but applications can still have:

- authentication bugs;
- authorization bugs;
- injection bugs;
- unsafe code defects;
- dependency vulnerabilities;
- cryptographic misuse;
- denial-of-service conditions;
- logic flaws.

Security is broader than the language's type system.

## 7. Observability

Production services should make important behavior visible through appropriate logs, metrics, and traces.

Design observability around:

- request IDs/correlation IDs;
- latency;
- error rates;
- resource saturation;
- queue depth;
- dependency health.

Avoid logging secrets, credentials, tokens, or personal data unnecessarily.

## 8. Command-line applications

Rust is well suited to CLI tooling because binaries are typically self-contained and startup/runtime overhead can be low. Build the CLI around a library when the logic could be reused or tested independently.

Suggested layers:

```text
CLI parsing
   ↓
application commands
   ↓
domain logic
   ↓
infrastructure adapters
```

## 9. Web/backend systems

Learn these concepts before choosing a specific framework:

- HTTP semantics;
- routing;
- request/response models;
- middleware;
- authentication/authorization;
- connection pooling;
- transactions;
- timeouts;
- retries and backoff;
- cancellation;
- rate limiting;
- observability.

Then evaluate the current ecosystem and framework docs rather than following an old tutorial verbatim.

## 10. Systems projects

To move beyond tutorial knowledge, build projects that force trade-offs.

### Level 1 — CLI

**Project:** File indexer

Features:

- recursively scan directories;
- ignore configured paths;
- hash files;
- persist an index;
- search by filename/hash;
- structured errors;
- tests.

### Level 2 — Service

**Project:** Concurrent job queue

Features:

- enqueue jobs;
- multiple workers;
- retry policy;
- backpressure;
- graceful shutdown;
- metrics;
- persistence.

### Level 3 — Network programming

**Project:** HTTP proxy/cache

Features:

- request parsing;
- upstream connections;
- caching;
- connection limits;
- timeouts;
- metrics;
- concurrent clients.

### Level 4 — Systems

**Project:** Key-value storage engine

Features:

- in-memory map;
- append-only log;
- recovery;
- compaction;
- checksums;
- concurrency control;
- benchmarks.

### Level 5 — Advanced

**Project:** Rust + C interoperability layer

Features:

- C ABI;
- `repr(C)` data structures;
- explicit ownership contracts;
- safe Rust wrapper;
- tests around invalid inputs;
- documented unsafe invariants.

## 11. Portfolio-quality project standard

For each serious project, maintain:

```text
README.md
ARCHITECTURE.md
CHANGELOG.md
LICENSE
Cargo.toml
src/
tests/
benches/              # when meaningful
.github/workflows/    # CI
```

The README should answer:

- What problem does this solve?
- Why Rust?
- What are the architecture decisions?
- How do I build it?
- How do I test it?
- What are the limitations?
- What are the performance characteristics?

## 12. Interview/reference questions

### Language

1. Explain move semantics.
2. Why are some types `Copy`?
3. What is the difference between `String` and `&str`?
4. What problem do lifetimes solve?
5. What are trait bounds?
6. When would you choose `dyn Trait`?
7. What are associated types?
8. Why are enums especially powerful in Rust?

### Memory

9. How does Rust prevent use-after-free in safe code?
10. What is borrowing?
11. Why is aliasing + mutation restricted?
12. What are `Box`, `Rc`, and `Arc`?
13. Why is interior mutability needed?

### Concurrency

14. What do `Send` and `Sync` mean?
15. Why does `Arc<Mutex<T>>` work across threads?
16. When would a channel be preferable?
17. What is a data race?
18. What is the difference between concurrency and parallelism?

### Async

19. What is a future?
20. What does `.await` do?
21. What is an executor?
22. Why is blocking code problematic inside async tasks?
23. What is cancellation?
24. Why does pinning exist?

### Unsafe

25. What does `unsafe` actually permit?
26. What is undefined behavior?
27. How do you document unsafe invariants?
28. What makes an FFI call unsafe?
29. Why use `repr(C)`?

### Production

30. How do you investigate a Rust performance regression?
31. How do you control dependency risk?
32. What belongs in CI?
33. How do you design library errors?
34. How do you keep public APIs stable?

## 13. Daily practice loop

Use a repeatable development cycle:

```text
Read one concept
   ↓
Write 20–50 lines of Rust
   ↓
Intentionally break it
   ↓
Read the compiler error
   ↓
Fix it without blindly cloning
   ↓
Write a test
   ↓
Run fmt + clippy + test
   ↓
Refactor for clarity
   ↓
Record what you learned
```

The most valuable Rust skill is learning to interpret the compiler as a design feedback system.

## 14. Recommended official study sequence

### Beginner

- Rust Book chapters 1–7
- Rust By Example for targeted practice
- Cargo fundamentals

### Intermediate

- Rust Book chapters on generics, traits, lifetimes, testing, I/O, functional features, and concurrency
- Standard library documentation
- API Guidelines

### Advanced

- Rust Reference
- Rustonomicon
- Async Book
- Compiler error explanations
- Rust Forge / compiler development material if compiler internals matter

## 15. Current official resource map

| Resource | Use it for |
|---|---|
| Rust Book | Main guided learning path |
| Rust Reference | Detailed syntax/semantics |
| Cargo Book | Package/build/dependency workflow |
| Rust By Example | Runnable examples |
| Standard Library docs | Exact API behavior |
| Edition Guide | Edition changes and migration |
| Async Book | Async concepts and ecosystem |
| Rustonomicon | Unsafe Rust and low-level invariants |
| Clippy docs | Lints and code-quality guidance |
| Rust Release Blog | Current stable releases |

## 16. Long-term maintenance

Rust evolves continuously. Revisit current official documentation when:

- adopting a newer stable compiler;
- switching editions;
- using newly stabilized language features;
- selecting an async runtime or major framework;
- reviewing unsafe patterns;
- preparing a library for a new MSRV policy.

Avoid freezing your understanding at one tutorial version.

## 17. Final milestone

You have reached a professional Rust level when you can independently:

```text
Design a domain model
      ↓
Choose ownership boundaries
      ↓
Define a trait-based API where justified
      ↓
Implement error handling
      ↓
Add unit + integration tests
      ↓
Use concurrency/async appropriately
      ↓
Profile real workloads
      ↓
Document public contracts
      ↓
Audit unsafe/FFI boundaries
      ↓
Ship through reproducible CI
```

## References

- Rust release announcements: https://blog.rust-lang.org/releases/
- Rust 1.98.0 (handbook baseline): https://blog.rust-lang.org/2026/08/20/Rust-1.98.0/
- Rust 1.100.0 (current stable): https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/
- Rust Book: https://doc.rust-lang.org/book/
- Reference: https://doc.rust-lang.org/stable/reference/
- Cargo: https://doc.rust-lang.org/cargo/
- Rust By Example: https://doc.rust-lang.org/rust-by-example/
- Async Book: https://rust-lang.github.io/async-book/
- Rustonomicon: https://doc.rust-lang.org/nomicon/
- API Guidelines: https://rust-lang.github.io/api-guidelines/
- Clippy: https://doc.rust-lang.org/stable/clippy/
- Install Rust: https://rust-lang.org/tools/install/
