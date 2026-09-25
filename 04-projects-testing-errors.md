# 04 — Project Architecture, Errors, Testing, and Documentation

## 1. Crate vs package

A **package** is a Cargo unit described by `Cargo.toml`. A package can contain one or more **crates** (libraries and/or binaries).

A library crate exposes reusable functionality. A binary crate produces an executable.

## 2. Practical layout

A small application can start as:

```text
my-app/
├── Cargo.toml
└── src/
    └── main.rs
```

A library-oriented project:

```text
my-lib/
├── Cargo.toml
└── src/
    ├── lib.rs
    ├── error.rs
    ├── parser.rs
    └── model.rs
```

A larger project may use workspace members:

```text
workspace/
├── Cargo.toml
├── crates/
│   ├── core/
│   ├── cli/
│   └── api/
└── tests/
```

## 3. Modules

Keep module boundaries aligned with responsibility and invariants, not arbitrary file size.

A useful rule:

> Put a type and the code that maintains its invariants behind the smallest practical visibility boundary.

## 4. Visibility

Everything is private by default.

Use `pub` intentionally. A public API is a long-term compatibility commitment.

Prefer exposing behavior instead of internal representation when invariants matter.

## 5. Error architecture

A useful distinction:

```text
Expected domain failure → typed Result error
Programmer invariant violation → panic may be justified internally
Fatal process condition → application-level termination
```

Libraries should normally return errors rather than terminating the process.

## 6. Custom errors

```rust
#[derive(Debug)]
pub enum ConfigError {
    MissingField(&'static str),
    InvalidPort(String),
    Io(std::io::Error),
}
```

Use `thiserror` or similar crates in production when appropriate, but learn manual error definitions first so you understand the underlying model.

## 7. Error propagation

```rust
fn load_config(path: &str) -> Result<String, std::io::Error> {
    let text = std::fs::read_to_string(path)?;
    Ok(text)
}
```

For applications, an application-level error type can aggregate lower-level causes.

## 8. Testing pyramid

### Unit tests

Test local behavior inside a module.

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn adds_values() {
        assert_eq!(2 + 3, 5);
    }
}
```

### Integration tests

Place external-facing tests under `tests/`.

### Documentation tests

Rust doc examples can be compiled and tested with Cargo. Rust By Example demonstrates `cargo test` and `cargo test --doc` as part of this workflow.

Reference: https://doc.rust-lang.org/rust-by-example/meta/doc.html

## 9. Test failure paths

Do not test only happy paths.

For a parser, test:

- empty input;
- malformed input;
- boundary values;
- invalid UTF-8 if raw bytes are accepted;
- oversized values;
- duplicate fields;
- unsupported versions.

## 10. Property-oriented thinking

Ask which invariant should always hold.

Example:

```text
parse(serialize(x)) == x
```

A property-testing library can explore many inputs, but even without one, writing the property down improves design quality.

## 11. Documentation

Rust documentation is generated from `///` comments:

```rust
/// Parses a port number from text.
///
/// # Errors
///
/// Returns an error if the value is outside the valid `u16` range.
pub fn parse_port(input: &str) -> Result<u16, std::num::ParseIntError> {
    input.parse()
}
```

Public documentation should communicate:

- what the function does;
- ownership and borrowing expectations;
- error behavior;
- panics, if any;
- safety requirements for unsafe functions;
- important performance characteristics.

## 12. Formatting and linting

Run:

```bash
cargo fmt
cargo clippy --all-targets --all-features
cargo test --all-targets
```

Clippy catches common correctness, suspicious, style, complexity, and performance issues. Its documentation warns against enabling the entire `restriction` category indiscriminately because individual restrictions can conflict or be unsuitable.

Reference: https://doc.rust-lang.org/stable/clippy/

## 13. Cargo workspaces

Workspaces are useful when multiple crates share a repository and dependency/build configuration.

Example:

```toml
[workspace]
members = [
    "crates/core",
    "crates/cli",
]
resolver = "3"
```

Keep domain logic in reusable library crates when multiple binaries or interfaces need it.

## 14. Feature flags

Features allow conditional compilation and optional dependencies.

Use features to keep a library flexible, but avoid creating a combinatorial explosion that becomes impossible to test.

## 15. Build profiles

Debug builds optimize developer feedback. Release builds optimize execution.

Use actual profiling to decide whether a release profile needs customization.

## 16. Dependency hygiene

Review dependencies for:

- maintenance activity;
- license compatibility;
- security advisories;
- transitive dependency count;
- compile-time impact;
- binary size impact;
- platform support;
- API stability.

Use `cargo tree` to understand why a dependency exists.

## 17. API design principles

Prefer:

- domain-specific types;
- explicit ownership semantics;
- minimal public surface;
- predictable errors;
- documented invariants;
- composable functions;
- sensible trait bounds.

Avoid:

- giant “utility” modules;
- public fields merely for convenience when invariants matter;
- generic abstractions with no concrete use case;
- `String` for every domain value;
- swallowing errors.

## 18. Exercises

### Project A — Config library

Create a library that loads configuration from a file and validates it. Include unit tests, integration tests, documentation tests, a custom error type, and a CLI example.

### Project B — Workspace

Create three crates:

```text
core domain
CLI adapter
HTTP adapter
```

The adapters should depend on the domain crate rather than the reverse.

### Project C — Library-quality crate

Pick a small utility that could be reused by other developers. Publish-style documentation should be generated with `cargo doc` and every public API item should have useful docs.

## 19. Architecture checkpoint

You should be able to open an unfamiliar Cargo workspace and explain:

```text
entrypoint → application/service layer → domain → infrastructure
                         ↓
                      errors
                         ↓
                      tests/docs
```

Do not force this exact architecture into every project. Treat it as a reasoning tool.

## References

- Cargo Book: https://doc.rust-lang.org/cargo/
- Rust API Guidelines: https://rust-lang.github.io/api-guidelines/
- Rust By Example — docs: https://doc.rust-lang.org/rust-by-example/meta/doc.html
- Clippy: https://doc.rust-lang.org/stable/clippy/
