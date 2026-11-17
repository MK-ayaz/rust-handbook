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


---

# 01 — Rust Fundamentals

> **Reading the snippets:** most examples show only the statements under discussion. Unless a `fn main()`
> wrapper is shown, assume the code lives inside one. Snippets marked `// invalid` are meant to fail to compile,
> and are there so you learn to read the error.

## 1. Rust's core idea

Rust is a systems programming language designed around performance, reliability, and memory safety without a garbage collector. Its distinctive model moves many correctness checks into compilation while still allowing low-level control. The official Rust Book describes this as balancing low-level control with high-level ergonomics.

Reference: https://doc.rust-lang.org/book/ch00-00-introduction.html

## 2. Mental model

Think of Rust as four systems working together:

1. **Types** describe what a value is allowed to represent.
2. **Ownership** determines who controls a value and when it is destroyed.
3. **Borrowing** allows temporary access without transferring ownership.
4. **Traits** describe shared behavior and constraints on generic code.

Rust's compiler, `rustc`, uses these rules to reject many classes of invalid programs before they run.

## 3. Variables

```rust
fn main() {
    let name = "Ayaz";
    let age = 30;

    let mut score = 10;
    score += 5;

    println!("{name} {age} {score}");
}
```

Bindings are immutable by default. `mut` is an explicit declaration that the binding can change.

### Shadowing

```rust
let value = 10;
let value = value + 5;
let value = "now a string";
```

Shadowing creates a new binding, so the type can change. Mutation changes the existing value and therefore must respect its type.

## 4. Scalar types

Common scalar types:

```rust
let signed: i32 = -42;
let unsigned: u64 = 42;
let float: f64 = 3.14;
let flag: bool = true;
let letter: char = 'R';
```

Choose integer widths intentionally at system boundaries, but do not over-specify every local variable without reason.

## 5. Compound types

### Tuple

```rust
let response: (u16, &str, bool) = (200, "OK", true);
let code = response.0;
```

### Array

```rust
let bytes: [u8; 4] = [1, 2, 3, 4];
```

Arrays have fixed length known at compile time.

### Slice

A slice such as `&[u8]` is a borrowed view into a contiguous sequence. It does not own the data.

## 6. Strings: the important distinction

Rust has two common string types:

```rust
let owned: String = String::from("hello");
let borrowed: &str = "hello";
```

`String` owns heap-allocated UTF-8 data. `&str` is a borrowed string slice. The distinction becomes central when designing APIs.

Prefer accepting `&str` when a function only needs to read text:

```rust
fn greet(name: &str) -> String {
    format!("Hello, {name}!")
}

fn main() {
    println!("{}", greet("Ada"));
}
```

## 7. Functions

```rust
fn add(left: i32, right: i32) -> i32 {
    left + right
}
```

The final expression can be returned without `return`.

Explicit return values make contracts visible. Use `return` mainly for early exits.

## 8. Control flow

### `if`

```rust
let score = 82;
let grade = if score >= 80 { "A" } else { "B" };
```

`if` is an expression, so it can produce a value. Both branches must produce compatible types.

### Loops

```rust
for number in 0..5 {
    println!("{number}");
}
```

Rust also has `while` and infinite `loop` expressions.

## 9. `match`

`match` is one of Rust's central control-flow tools.

```rust
let status = 200;

match status {
    200..=299 => println!("success"),
    400..=499 => println!("client error"),
    500..=599 => println!("server error"),
    _ => println!("other"),
}
```

Patterns are checked for exhaustiveness. This is a major reason enums are so powerful in Rust.

## 10. Structs

```rust
struct User {
    id: u64,
    name: String,
    active: bool,
}

fn main() {
    let user = User {
        id: 1,
        name: String::from("Ada"),
        active: true,
    };

    println!("{} {}", user.id, user.name);
}
```

Structs let you model domain data explicitly.

## 11. Methods and `impl`

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}
```

`&self` means the method borrows the instance. Other receivers include `&mut self` and `self`.

## 12. Enums

```rust
enum PaymentStatus {
    Pending,
    Paid { transaction_id: String },
    Failed(String),
}
```

Enums represent a value that can be one of several variants. This is ideal for protocol states, application states, parser output, domain errors, and state machines.

## 13. `Option<T>`

Rust uses `Option<T>` instead of a null value for an optional value.

```rust
fn find_user(id: u64) -> Option<String> {
    if id == 1 {
        Some(String::from("Ada"))
    } else {
        None
    }
}
```

Consume it with pattern matching or combinators:

```rust
let name = find_user(1).unwrap_or_else(|| "Unknown".to_string());
```

Use `unwrap_or_else` when a fallback must be computed lazily.

## 14. `Result<T, E>`

Fallible operations typically return `Result<T, E>`.

```rust
fn parse_port(input: &str) -> Result<u16, std::num::ParseIntError> {
    input.parse()
}
```

This separates successful output from an explicit error path.

## 15. The `?` operator

```rust
fn load_port(input: &str) -> Result<u16, std::num::ParseIntError> {
    let port = input.parse::<u16>()?;
    Ok(port)
}
```

`?` propagates an error from the surrounding function. It is one of the most important tools for readable error handling.

## 16. Collections

### `Vec<T>`

```rust
let mut users = Vec::new();
users.push("Ada");
users.push("Grace");
```

### `HashMap<K, V>`

```rust
use std::collections::HashMap;

let mut counts = HashMap::new();
counts.insert("rust", 3);
```

### Iteration

```rust
for user in &users {
    println!("{user}");
}
```

Borrowing the collection avoids moving its elements.

## 17. Closures

```rust
let double = |x: i32| x * 2;
println!("{}", double(21));
```

Closures can capture values from their environment. Rust infers whether a closure needs immutable borrowing, mutable borrowing, or ownership based on what the closure does.

## 18. Iterators

```rust
let total: i32 = (1..=5)
    .filter(|n| n % 2 == 1)
    .map(|n| n * 10)
    .sum();
```

Iterator adapters are lazy; the terminal operation such as `sum`, `collect`, `for_each`, or `fold` drives evaluation.

## 19. Modules and visibility

```rust
mod math {
    pub fn add(a: i32, b: i32) -> i32 {
        a + b
    }
}

fn main() {
    println!("{}", math::add(2, 3));
}
```

Items are private by default. `pub` exposes them to the appropriate module boundary.

## 20. Cargo fundamentals

Cargo is Rust's package manager and build system. It downloads dependencies, compiles crates, runs tests, creates documentation, and packages projects for publication.

Useful commands:

```bash
cargo new app
cargo init
cargo check
cargo test
cargo run
cargo build --release
cargo fmt
cargo clippy
cargo doc --open
cargo tree
```

Reference: https://doc.rust-lang.org/cargo/

## 21. Exercises

### Exercise A — CLI calculator

Build a command-line calculator with:

- addition, subtraction, multiplication, division;
- integer parsing with `Result`;
- a custom error enum;
- tests for valid and invalid input.

### Exercise B — Log analyzer

Read a text file, count status codes, and print the top five codes. Do not use `unwrap()` on file reads or parsing.

### Exercise C — Domain model

Create an order model with:

```text
Order
 ├── id
 ├── customer
 ├── items
 └── status: Pending | Paid | Cancelled
```

Use enums instead of magic strings for status.

## 22. Fundamentals checklist

- [ ] Variables and mutability
- [ ] Scalar and compound types
- [ ] Functions and expressions
- [ ] `if`, loops, and `match`
- [ ] Structs and methods
- [ ] Enums and pattern matching
- [ ] `Option` and `Result`
- [ ] `?` error propagation
- [ ] `String` vs `&str`
- [ ] `Vec`, `HashMap`, slices
- [ ] Closures and iterators
- [ ] Modules and visibility
- [ ] Cargo workflow

## References

- The Rust Programming Language: https://doc.rust-lang.org/book/
- Rust By Example: https://doc.rust-lang.org/rust-by-example/
- Standard library: https://doc.rust-lang.org/std/


---

# 02 — Ownership, Borrowing, and Lifetimes

This is the most important conceptual section in Rust.

## 1. Ownership in one sentence

Every owned value has a single owner, and when the owner goes out of scope, the value is dropped.

The exact rules matter more than the slogan:

1. Each value has an owner.
2. There can be one owner at a time.
3. When the owner goes out of scope, the value is dropped.

The Rust Book introduces ownership as the mechanism that enables memory safety without a garbage collector.

Reference: https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html

## 2. Move semantics

```rust
let first = String::from("hello");
let second = first;
```

`String` is not `Copy`. Ownership moves to `second`. Using `first` afterward is rejected.

This prevents two owners from freeing the same heap allocation.

## 3. Copy types

Simple stack-only values such as integers can implement `Copy`.

```rust
let a = 10;
let b = a;
println!("{a} {b}");
```

For `Copy` types, assignment creates a copy rather than transferring ownership.

## 4. Clone is explicit duplication

```rust
let first = String::from("hello");
let second = first.clone();
```

`clone()` is an explicit request to duplicate data. It may allocate and copy significant amounts of memory. Never use cloning as an automatic response to a borrow checker error without understanding the ownership requirement.

## 5. Borrowing

A reference temporarily accesses a value without taking ownership.

```rust
fn length(value: &String) -> usize {
    value.len()
}
```

Usually prefer `&str` rather than `&String` when a function needs only string contents:

```rust
fn length(value: &str) -> usize {
    value.len()
}
```

This accepts both string literals and `String` values via borrowing/coercion.

## 6. Mutable references

```rust
fn append_exclamation(value: &mut String) {
    value.push('!');
}
```

A mutable reference permits mutation through that reference.

Rust's aliasing discipline can be summarized as:

> You may have many shared immutable references, or one mutable reference, but not both at the same time for the same data under the same borrow rules.

This rule is fundamental to preventing data races in safe Rust.

## 7. Why references cannot outlive values

This is invalid:

```rust
// invalid
fn broken() -> &String {
    let value = String::from("hello");
    &value
}
```

`value` is destroyed when the function returns. Returning a reference to it would create a dangling reference.

Rust rejects the program rather than letting undefined behavior occur.

## 8. Slices

A slice is a borrowed region of a collection.

```rust
fn first_word(text: &str) -> &str {
    text.split_whitespace().next().unwrap_or("")
}
```

For arrays:

```rust
let numbers = [10, 20, 30, 40];
let part = &numbers[1..3];
```

## 9. Lifetimes: what they actually mean

A lifetime is a region of code during which a reference is valid. Lifetime annotations do not extend an object's life; they describe relationships that already exist.

Example:

```rust
fn longest<'a>(left: &'a str, right: &'a str) -> &'a str {
    if left.len() >= right.len() { left } else { right }
}
```

The annotation states that the returned reference is valid for no longer than the shorter relevant input lifetime.

## 10. Lifetime elision

You often do not write lifetime annotations because Rust has deterministic elision rules.

This:

```rust
fn first(text: &str) -> &str {
    text
}
```

can be written without an explicit `'a` because the elision rules supply it. The rules are:

1. Every elided input lifetime becomes its own fresh lifetime parameter.
2. If there is **exactly one** input lifetime, it is assigned to all elided output lifetimes.
3. If there are multiple input lifetimes but one of them is `&self` or `&mut self`, `self`'s lifetime is
   assigned to all elided output lifetimes.

If none of those rules determine an output lifetime, the compiler requires an explicit annotation. Note that
`fn first(text: &str, suffix: &str) -> &str` fails to compile precisely because rule 2 no longer applies and
rule 3 has no `self`.

## 11. Structs with references

A struct that stores a reference must describe the lifetime relationship.

```rust
struct UserView<'a> {
    name: &'a str,
}
```

Read this as: `UserView` cannot outlive the string slice stored in `name`.

## 12. `String` vs `&str`: API design

Prefer:

```rust
fn validate_name(name: &str) -> bool
```

when the function does not need ownership.

Prefer:

```rust
fn set_name(name: String)
```

when the object is taking ownership as part of its state.

Prefer returning `String` when the function creates owned output.

## 13. Ownership through function calls

```rust
fn consume(value: String) {}

let name = String::from("Ada");
consume(name);
// name is moved
```

Use borrowing when ownership is unnecessary:

```rust
fn inspect(value: &str) {}

let name = String::from("Ada");
inspect(&name);
// name remains usable
```

## 14. Returning ownership

Rust functions can cleanly transfer ownership back:

```rust
fn create_name() -> String {
    String::from("Ada")
}

let name = create_name();
```

This is common and efficient. Do not assume that returning a `String` means copying all its bytes.

## 15. The borrow checker's questions

When the compiler rejects code, ask these questions in order:

1. Who owns this value?
2. Does this operation move it?
3. Does this reference need to remain valid later?
4. Is a mutable borrow active while another borrow exists?
5. Could I change the function to borrow instead of own?
6. Could I make the data ownership explicit by restructuring the code?
7. Is cloning actually part of the domain requirement?

## 16. Non-lexical lifetimes

Modern Rust reasons about when references are actually used rather than simply using the entire lexical scope. This often allows code such as:

```rust
let mut value = String::from("hello");
let len = value.len();
value.push('!');
println!("{len} {value}");
```

The immutable borrow used to calculate `len` ends before the mutation is required.

### Edition 2024 temporary-scope changes

Two drop-timing rules changed in the 2024 Edition, and both are visible through the borrow checker:

- **`if let` temporaries** in the scrutinee are dropped before the `else` block in 2024, rather than at the end
  of the whole `if let`. This lets you mutate a value in `else` that the scrutinee borrowed.
- **Tail-expression temporaries** are dropped before the function's local variables in 2024. A temporary created
  in the final expression of a block no longer outlives the locals of that block.

## 17. Interior mutability

Rust normally enforces mutation through `&mut`. Interior mutability provides controlled mutation through shared references using types such as:

- `Cell<T>`
- `RefCell<T>`
- `Mutex<T>`
- `RwLock<T>`
- atomics

Each solves a different problem and has different runtime or synchronization costs.

## 18. Smart pointers

### `Box<T>`

Stores a value on the heap while retaining unique ownership.

```rust
let value = Box::new(42);
```

Useful for recursive data structures and explicit heap allocation.

### `Rc<T>`

Reference-counted shared ownership for single-threaded code. The reference count is a plain integer, so `Rc<T>`
is deliberately `!Send` and `!Sync`; sharing it across threads would race on the count.

### `Arc<T>`

Atomically reference-counted shared ownership for multi-threaded code.

`Arc<T>` implements `Send` and `Sync` only when `T: Send + Sync`. The atomic count makes the *count* safe to
share, but it says nothing about the value inside: to mutate shared data you still combine it with a lock, as in
`Arc<Mutex<T>>` or `Arc<RwLock<T>>`.

## 19. Designing around ownership

Bad strategy:

```text
Compiler error → add clone() → compiler stops complaining
```

Better strategy:

```text
Compiler error
   ↓
Identify owner
   ↓
Identify required lifetime
   ↓
Decide ownership vs borrow
   ↓
Restructure API/data flow
   ↓
Clone only when duplication is semantically required
```

## 20. Advanced ownership patterns

### Borrowing multiple fields

Sometimes the borrow checker cannot infer that two fields are independent through a particular expression. Split borrows explicitly or destructure the value so the disjointness is visible.

### Ownership transfer in iterators

Compare:

```rust
for item in values.iter() {}
for item in values.iter_mut() {}
for item in values.into_iter() {}
```

These correspond broadly to shared borrowing, mutable borrowing, and consuming ownership.

### `mem::take` and `mem::replace`

These tools help move a field out while leaving a valid replacement behind.

```rust
use std::mem;

fn take_buffer(buffer: &mut Vec<u8>) -> Vec<u8> {
    mem::take(buffer)
}
```

## 21. Exercises

### Exercise A — Fix ownership without cloning

Given a function that repeatedly clones `String` values to satisfy the compiler, redesign it to borrow or transfer ownership appropriately.

### Exercise B — Build a text index

Store document contents and expose functions returning slices into the stored text where lifetime relationships permit it.

### Exercise C — State machine

Create a connection type with states such as `Disconnected`, `Connecting`, and `Connected`, and use ownership to prevent invalid transitions.

## 22. Mastery questions

You should be able to answer these without running the code:

1. Why does assigning a `String` move it?
2. Why can an integer usually be copied?
3. Why is `&String` often weaker than `&str` as an API parameter?
4. Why can't a function return a reference to a local variable?
5. What does a lifetime annotation communicate?
6. Why is `Rc<T>` single-threaded?
7. Why might `Arc<T>` still need a `Mutex<T>`?
8. When is cloning the correct semantic operation?

## References

- Ownership chapter: https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html
- References and borrowing: https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html
- Lifetimes: https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html
- Rust Reference: https://doc.rust-lang.org/stable/reference/


---

# 03 — Types, Traits, Generics, and Zero-Cost Abstractions

> **Reading the snippets:** examples show the item or statement under discussion, not always a complete
> program. Assume free-standing statements live inside a function such as `fn main()`.

## 1. Rust's type-system mindset

Rust encourages you to make invalid states difficult or impossible to represent. Strong domain types often remove entire classes of runtime checks.

A useful progression is:

```text
primitive → struct/enum → generic → trait → abstraction boundary
```

## 2. Newtype pattern

```rust
struct UserId(u64);
struct OrderId(u64);
```

Now a function can require `UserId` instead of an arbitrary `u64`.

This prevents accidental mixing of semantically different identifiers.

## 3. Type aliases vs newtypes

Alias:

```rust
type UserId = u64;
```

Newtype:

```rust
struct UserId(u64);
```

An alias improves readability but does not create a distinct type. A newtype creates a distinct type and therefore stronger compile-time guarantees.

## 4. Generics

```rust
fn first<T>(items: &[T]) -> Option<&T> {
    items.first()
}
```

Generics express reusable algorithms without sacrificing static typing.

## 5. Trait bounds

```rust
fn print_value<T: std::fmt::Display>(value: T) {
    println!("{value}");
}
```

A trait bound says what behavior a generic type must provide.

Equivalent `where` syntax:

```rust
fn print_value<T>(value: T)
where
    T: std::fmt::Display,
{
    println!("{value}");
}
```

Use `where` clauses when bounds become complex enough that the function signature is easier to read when separated.

## 6. Define your own traits

```rust
trait CacheKey {
    fn key(&self) -> String;
}

struct User {
    id: u64,
}

impl CacheKey for User {
    fn key(&self) -> String {
        format!("user:{}", self.id)
    }
}
```

Traits define behavior contracts, not inheritance hierarchies.

## 7. Trait objects

Generic dispatch:

```rust
fn run<T: CacheKey>(value: &T) {
    println!("{}", value.key());
}
```

Trait-object dispatch:

```rust
fn run(value: &dyn CacheKey) {
    println!("{}", value.key());
}
```

Use generics when the concrete type matters to compilation/performance. Use `dyn Trait` when dynamic heterogeneity is genuinely required.

## 8. Associated types

```rust
trait IteratorLike {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}
```

Associated types are useful when a trait implementation has one natural associated type.

## 9. Associated constants and functions

Traits can also define associated constants and associated functions, allowing APIs to express compile-time metadata and constructors without an instance.

## 10. Derive macros

Common derives:

```rust
#[derive(Debug, Clone, PartialEq, Eq)]
struct User {
    id: u64,
}
```

Derives generate implementations for common traits.

Do not derive traits simply because they are available. For example, `Clone` communicates that duplication is meaningful.

## 11. Pattern matching deeply

```rust
enum Command {
    Move { x: i32, y: i32 },
    Print,
    Quit,
}

fn execute(command: Command) {
    match command {
        Command::Move { x, y } => println!("move {x} {y}"),
        Command::Print => println!("print"),
        Command::Quit => println!("quit"),
    }
}
```

Pattern matching can destructure structs, tuples, enums, references, and ranges.

## 12. `if let` and `let else`

Use `if let` when you only care about one pattern:

```rust
if let Some(value) = option {
    println!("{value}");
}
```

Use `let ... else` when the successful path should remain linear:

```rust
let Some(value) = option else {
    return;
};
println!("{value}");
```

## 13. Iterators and ownership

Important methods include:

```text
iter        -> shared borrow
iter_mut    -> mutable borrow
into_iter   -> consume/own
map         -> transform
filter      -> select
filter_map  -> select + transform
flat_map    -> flatten
fold        -> accumulate
collect     -> materialize
```

The exact item type of each iterator matters. Learn to inspect it rather than guessing.

## 14. `collect` and type inference

```rust
let values: Vec<i32> = (1..=5).collect();
```

When inference needs help:

```rust
let values = (1..=5).collect::<Vec<_>>();
```

The `_` asks the compiler to infer the element type while you specify the collection type.

## 15. Closures as values

Closures have anonymous compiler-generated types. Traits such as `Fn`, `FnMut`, and `FnOnce` describe how a closure can be invoked based on what it captures.

Broadly:

- `Fn`: callable through shared access.
- `FnMut`: may mutate captured state.
- `FnOnce`: may consume captured state.

A closure can implement more than one of these traits depending on its behavior.

## 16. Function pointers

A normal function can be passed as a function pointer:

```rust
fn square(x: i32) -> i32 {
    x * x
}

let f: fn(i32) -> i32 = square;
```

Use function pointers when a plain function is sufficient; use generic closure parameters when callers need captured state.

## 17. Generic data structures

```rust
struct Pair<T> {
    left: T,
    right: T,
}
```

You can constrain behavior separately:

```rust
impl<T: PartialEq> Pair<T> {
    fn same(&self) -> bool {
        self.left == self.right
    }
}
```

## 18. Phantom types

Phantom types encode compile-time state without storing extra runtime data.

```rust
use std::marker::PhantomData;

struct Connection<State> {
    id: u64,
    _state: PhantomData<State>,
}
```

This pattern becomes powerful in protocol/state-machine APIs.

## 19. Sealed traits

Library authors sometimes use a private/sealed trait pattern to prevent external crates from implementing a public trait. This preserves API invariants and future evolution room.

## 20. Type-state pattern

Represent legal states through distinct types:

```rust
struct Closed;
struct Open;

struct FileHandle<State> {
    fd: i32,
    _state: std::marker::PhantomData<State>,
}
```

Methods can be implemented only on the relevant state.

## 21. Macros

Rust has declarative macros such as `macro_rules!` and procedural macros.

Use macros when the problem is genuinely syntactic/code-generative. Do not reach for a macro when a function, trait, generic, or module gives clearer semantics.

## 22. Error types as domain types

```rust
#[derive(Debug)]
enum PaymentError {
    InvalidAmount,
    Network(String),
    Declined,
}
```

Strong error enums help callers distinguish recoverable cases from unexpected failures.

## 23. Exercises

### Exercise A — Generic repository

Create a generic repository abstraction supporting insert, get, delete, and list operations.

### Exercise B — Pluggable formatter

Define a `Formatter` trait and implement JSON-like, text, and compact formats. Use both generic and `dyn Formatter` versions, then explain the trade-offs.

### Exercise C — Type-state resource

Implement a resource that cannot execute an operation until it has been initialized. Represent the state transition in the type system.

## 24. Mastery checklist

- [ ] Newtypes
- [ ] Generic functions and structs
- [ ] Trait definitions and implementations
- [ ] Trait bounds and `where`
- [ ] `dyn Trait`
- [ ] Associated types
- [ ] Derive macros
- [ ] Pattern destructuring
- [ ] `Fn`, `FnMut`, `FnOnce`
- [ ] Iterator ownership semantics
- [ ] Type-state pattern
- [ ] Macro basics

## References

- Generics: https://doc.rust-lang.org/book/ch10-00-generics.html
- Traits: https://doc.rust-lang.org/book/ch10-02-traits.html
- Advanced types: https://doc.rust-lang.org/book/ch20-03-advanced-types.html
- Rust Reference: https://doc.rust-lang.org/stable/reference/


---

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

`resolver = "3"` is the default for Edition 2024 (it requires Rust 1.84+), and it enables MSRV-aware dependency
selection. In a single package the resolver is inferred from `edition = "2024"`, but a **virtual workspace** has
no edition of its own, so the resolver must be set explicitly here.

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


---

# 05 — Concurrency and Async Rust

## 1. Two different problems

**Concurrency** asks how multiple computations can make progress together.

**Parallelism** asks how computations can physically execute at the same time on multiple CPU cores.

**Async programming** is a cooperative concurrency model where tasks yield so an executor can run other tasks.

Rust supports all of these, but the ownership/type system constrains how data can cross boundaries.

> **Note on examples:** snippets in this chapter show the interesting statements only. Assume each one lives
> inside `fn main()` (or a helper `fn`) and that `unwrap()` is used to keep the example short, not as a
> recommendation for production error handling.

## 2. Threads

```rust
use std::thread;

let handle = thread::spawn(|| {
    println!("worker");
});

handle.join().unwrap();
```

A spawned thread can own moved data:

```rust
use std::thread;

let message = String::from("hello");

let handle = thread::spawn(move || {
    println!("{message}");
});

handle.join().unwrap();
```

The `move` closure explicitly transfers ownership into the thread.

### Scoped threads

`thread::spawn` requires `'static` data, which forces `move` plus `Arc` when you want to lend a value to a
thread. `std::thread::scope` (stable since Rust 1.63) lets threads borrow non-`'static` data, because the
scope guarantees they are joined before it returns:

```rust
use std::thread;

let data = vec![1, 2, 3, 4];

thread::scope(|scope| {
    let left = &data[..2];
    let right = &data[2..];

    scope.spawn(|| println!("left: {left:?}"));
    scope.spawn(|| println!("right: {right:?}"));
});
// All threads have finished; `data` is usable again.
```

Prefer a scope when the parent outlives the workers and you do not need detached threads.

## 3. Channels

Channels transfer messages between producers and consumers.

```rust
use std::sync::mpsc;
use std::thread;

let (tx, rx) = mpsc::channel();

thread::spawn(move || {
    tx.send(String::from("hello")).unwrap();
});

let message = rx.recv().unwrap();
println!("{message}");
```

The important design question is often not “how do I share this data?” but “can I transfer ownership instead?”

## 4. `Send` and `Sync`

`Send`: a type can be safely transferred to another thread.

`Sync`: a type can be safely referenced from multiple threads; formally, `T: Sync` means `&T: Send`.

These marker traits are fundamental to Rust's thread-safety model. Incorrect implementations of unsafe marker traits can cause undefined behavior, so they are tightly controlled.

Reference: https://doc.rust-lang.org/nomicon/send-and-sync.html

## 5. Shared mutable state

For shared state, a common pattern is:

```text
Arc<T>
  +
Mutex<T>
```

Example:

```rust
use std::sync::{Arc, Mutex};
use std::thread;

let count = Arc::new(Mutex::new(0));
let mut handles = Vec::new();

for _ in 0..4 {
    let count = Arc::clone(&count);
    handles.push(thread::spawn(move || {
        let mut guard = count.lock().unwrap();
        *guard += 1;
    }));
}

for handle in handles {
    handle.join().unwrap();
}
```

`Arc` handles shared ownership across threads. `Mutex` provides mutual exclusion for mutable access.

## 6. `RwLock`

Use `RwLock` when many readers can progress concurrently but writers require exclusive access. Do not assume it is automatically faster than `Mutex`; workload and contention matter.

## 7. Atomics

Atomics are useful for small shared state such as counters, flags, and lock-free coordination. They require a strong understanding of memory ordering before being used for complex algorithms.

Treat `Ordering` as a correctness question, not a micro-optimization.

## 8. Message passing vs shared state

Message passing often simplifies reasoning because ownership is transferred.

Shared state can be appropriate when many operations must observe or update the same resource.

Choose based on data ownership and synchronization needs rather than ideology.

## 9. Async fundamentals

An `async fn` does not immediately execute its body to completion. It produces a future representing asynchronous work. An executor polls futures and coordinates when they make progress.

The Async Book describes the ecosystem this way and notes that async runtimes are crates that manage tasks and scheduling.

Reference: https://rust-lang.github.io/async-book/

## 10. Basic async shape

Using an executor/runtime:

```rust
async fn load_data() -> Result<String, std::io::Error> {
    // asynchronous operations
    Ok(String::from("data"))
}
```

The exact runtime—such as Tokio or another executor—is an ecosystem choice. Learn the language-level future model separately from the runtime API.

## 11. `.await`

```rust
async fn process() {
    let data = load_data().await;
    println!("{data:?}");
}
```

`.await` suspends the current async task when the future is not ready and allows the executor to make progress elsewhere.

## 12. Async is not “threads but smaller”

A thread is scheduled by the operating system. An async task is typically scheduled by an executor.

Async is especially effective for I/O-heavy workloads with many concurrent operations. CPU-heavy work may still need dedicated threads or a blocking pool.

The Async Book explicitly warns about blocking I/O inside async functions because blocking can prevent useful progress by the runtime.

## 13. Tasks

Runtimes provide APIs to spawn independent asynchronous tasks. A task should generally be treated as a lightweight unit of concurrent work, not an OS thread.

## 14. Cancellation

Async Rust requires you to reason about what happens when a future is dropped before completion.

Ask:

- What resources are held?
- Is partial work safe?
- Is a request cancellation-safe?
- Does dropping a future close a socket, release a lock, or leave an external operation running?

## 15. Pinning

Some asynchronous state machines become self-referential after compilation. `Pin` and `Unpin` are part of Rust's mechanism for expressing whether a value may move in memory.

Do not learn pinning as a collection of memorized syntax. First understand why some futures need stable memory addresses.

## 16. Async trait considerations

Async methods in traits have evolved substantially, but ecosystem ergonomics and object-safety constraints still matter. Always check the current compiler and runtime/library support rather than relying on old blog posts.

The Async Book itself notes some async-trait-related rough edges, so treat its caveats as living documentation rather than a frozen specification.

## 17. Blocking boundaries

A robust service architecture often looks like:

```text
async task
   ↓
async network / storage
   ↓
CPU-heavy or blocking work
   ↓
dedicated blocking/thread pool
```

The exact mechanism depends on the runtime.

## 18. Concurrency testing

Concurrency bugs are often schedule-dependent. Use deterministic designs where possible, keep critical sections small, and test invariants rather than trying to “sleep and hope” a race appears.

## 19. Exercises

### Exercise A — Parallel file processor

Spawn worker threads to process files and send structured results through a channel.

### Exercise B — Shared metrics

Build a multi-threaded counter using `Arc<Mutex<_>>`, then implement a version using atomics. Explain the trade-off.

### Exercise C — Async fetch pipeline

Build a program that concurrently requests multiple resources, limits concurrency, aggregates failures, and reports timing.

### Exercise D — Cancellation-safe operation

Design an async operation that owns a temporary resource and prove what happens when the future is dropped midway.

## 20. Mastery questions

1. What does `Send` guarantee?
2. What does `Sync` guarantee?
3. Why does `Arc<T>` solve ownership but not mutable synchronization?
4. When is a channel better than a mutex?
5. What does `.await` actually do to task execution?
6. Why is blocking work dangerous inside async tasks?
7. What problem does pinning solve?
8. Why can CPU-bound work require different execution strategies than I/O-bound work?

## References

- The Rust Book — concurrency: https://doc.rust-lang.org/book/ch16-00-concurrency.html
- Async Book: https://rust-lang.github.io/async-book/
- Rustonomicon — Send/Sync: https://doc.rust-lang.org/nomicon/send-and-sync.html


---

# 06 — Advanced Rust, Unsafe, FFI, and Performance

## 1. When to study this section

Only after you are comfortable with ownership, lifetimes, traits, testing, and concurrency.

Advanced Rust is not a badge. It is a toolbox for cases where safe, simple Rust cannot express the required system boundary or performance behavior.

## 2. What `unsafe` changes

Unsafe Rust permits a small set of operations the compiler cannot fully verify, including raw-pointer dereference, calling unsafe functions, implementing unsafe traits, mutable static access, and union field access.

The Rustonomicon emphasizes that `unsafe` does not turn off all safety checking. It creates a boundary around operations whose contracts must be upheld by the programmer.

Reference: https://doc.rust-lang.org/nomicon/what-unsafe-does.html

### Edition 2024 changes to `unsafe`

If you are writing 2024 Edition code, three rules differ from older material:

1. **`extern` blocks must be declared `unsafe extern`** (`missing_unsafe_on_extern` lint). Functions in an
   `extern` block are implicitly unsafe; add the `safe` qualifier only to bindings you have audited.
2. **`unsafe_op_in_unsafe_fn` is warn-by-default.** The body of an `unsafe fn` is no longer an implicit
   `unsafe` block; you must write an explicit unsafe block inside it.
3. **Unsafe attributes require the `unsafe(...)` wrapper:** `#[unsafe(no_mangle)]`,
   `#[unsafe(export_name = "...")]`, `#[unsafe(link_section = "...")]`.

## 3. Safety invariants

When writing unsafe code, document the invariant that makes the operation valid.

Bad:

```rust
unsafe {
    // trust me
}
```

Better:

```rust
/// # Safety
/// `ptr` must be non-null, properly aligned, and point to a valid `T`
/// that stays valid for the duration of the call.
unsafe fn read_once<T>(ptr: *const T) -> T {
    // SAFETY:
    // `ptr` is non-null, properly aligned, points to a live `T`,
    // and is valid for reads for the duration of this operation.
    unsafe { ptr.read() }
}
```

The comment is not a substitute for proof. It records the contract that must be reviewed and maintained.

## 4. Scope unsafe narrowly

Prefer keeping validation in safe code and the unsafe region minimal:

```rust
pub fn first_u32_le(bytes: &[u8]) -> Result<u32, &'static str> {
    let first_four = bytes.get(..4).ok_or("need at least 4 bytes")?;
    let array: [u8; 4] = first_four.try_into().unwrap();
    Ok(u32::from_le_bytes(array))
}
```

A small unsafe core surrounded by safe validation is easier to audit than a giant unsafe module.

The Rustonomicon specifically discusses restricting unsafe code and building safe abstractions around verified invariants.

Reference: https://doc.rust-lang.org/nomicon/working-with-unsafe.html

## 5. Raw pointers

Rust has raw pointer types:

```rust
let x = 5i32;
let ptr: *const i32 = &x as *const i32;

let mut y = 6i32;
let mut_ptr: *mut i32 = &mut y as *mut i32;
```

Creating them is safe. Dereferencing them is unsafe because the compiler cannot prove validity, alignment, aliasing, or lifetime correctness in the general case.

## 6. Undefined behavior

Undefined behavior is not “the program crashed.” It means the program violated assumptions that the compiler is allowed to rely on, potentially allowing arbitrary optimization consequences.

Do not use unsafe operations merely to silence the borrow checker.

## 7. FFI

FFI means Foreign Function Interface: calling code across language/ABI boundaries.

Rust's FFI module documents utilities for interoperating with non-Rust interfaces. C strings differ from Rust strings in encoding and termination rules; conversions must respect the foreign API's contract.

Reference: https://doc.rust-lang.org/std/ffi/

## 8. `extern`

An external function declaration communicates an ABI boundary. Calling foreign functions is unsafe because Rust cannot verify what the foreign code will do.

In Rust 2024 the block itself must be marked `unsafe extern`:

```rust
// Edition 2024: the whole block is `unsafe extern`.
unsafe extern "C" {
    // Implicitly unsafe to call.
    fn abs(input: i32) -> i32;
    // Opt in explicitly when you have audited the binding.
    safe fn strlen(ptr: *const std::ffi::c_char) -> usize;
}

fn distance_to_zero(value: i32) -> i32 {
    // SAFETY: `abs` takes a plain i32 and has no other contract to uphold.
    unsafe { abs(value) }
}
```

The current Rust Reference documents external blocks and FFI syntax: https://doc.rust-lang.org/reference/items/external-blocks.html

## 9. FFI checklist

Before crossing the boundary, verify:

- ABI is correct;
- argument layout is correct;
- ownership rules are explicit;
- lifetimes are valid;
- alignment is valid;
- nullability is handled;
- strings and encoding are correct;
- who allocates and who frees memory is documented;
- thread-safety assumptions are correct;
- panics do not cross unsupported foreign boundaries.

## 10. `repr(C)`

When interoperating with C-compatible layouts, use the appropriate representation attributes and mirror the foreign layout precisely.

```rust
#[repr(C)]
struct Point {
    x: i32,
    y: i32,
}
```

Do not assume Rust's default struct layout is suitable for foreign ABI contracts.

An exported function that a C caller will link against is written like this in Edition 2024:

```rust
#[unsafe(no_mangle)]
pub extern "C" fn point_manhattan_distance(a: Point, b: Point) -> i32 {
    (a.x - b.x).abs() + (a.y - b.y).abs()
}
```

## 11. Performance starts with measurement

Use this order:

```text
Correctness
  ↓
Workload definition
  ↓
Measurement
  ↓
Profile
  ↓
Change one thing
  ↓
Measure again
```

Avoid optimizing based solely on intuition.

## 12. Allocation awareness

Important questions:

- How many heap allocations occur?
- Are allocations inside hot loops?
- Can a buffer be reused?
- Can a borrow replace an owned temporary?
- Is data copied between layers unnecessarily?
- Is a `Vec` capacity known in advance?

Use `with_capacity` when the size estimate is reliable:

```rust
let mut values = Vec::with_capacity(1024);
```

Do not preallocate blindly everywhere; measure whether it matters.

## 13. Zero-copy design

Instead of repeatedly creating owned strings, parsers can often return slices into an existing input buffer when lifetimes and ownership allow.

The trade-off is API complexity and input-buffer lifetime coupling. Zero-copy is a design choice, not an automatic virtue.

## 14. Cache behavior

Performance can depend more on memory access patterns than algorithmic instruction counts for some workloads.

Think about:

- contiguous data;
- cache locality;
- pointer chasing;
- branch predictability;
- allocation frequency;
- data layout.

## 15. Generics and monomorphization

Generic functions are commonly specialized for concrete types during compilation. This can enable efficient static dispatch, but excessive generic complexity can increase compile times and binary size.

Use dynamic dispatch where it improves architecture or code size without creating a performance problem.

## 16. Benchmarks

Use a benchmark framework appropriate to the current Rust ecosystem. Benchmark realistic workloads, not only micro-expressions that disappear under compiler optimization.

A useful benchmark compares complete relevant operations:

```text
input → parsing → transformation → output
```

## 17. Release builds

Always profile performance-sensitive code with an optimized build. Debug performance can be dramatically different.

## 18. Compiler diagnostics

Use:

```bash
rustc --explain <error-code>
```

when the compiler gives a diagnostic code. The official Rust documentation includes extended explanations for many error codes.

## 19. Advanced language topics to study next

- trait coherence and the orphan rules;
- variance;
- higher-ranked trait bounds;
- associated types and generic associated types;
- auto traits;
- `Send`/`Sync` implementation details;
- `Pin` and self-referential futures;
- macro hygiene;
- declarative vs procedural macros;
- specialization-related design constraints;
- drop checking;
- allocator APIs and custom allocation strategies where justified.

The Reference is the better source for exact language semantics; the Rustonomicon is the companion for advanced unsafe patterns.

## 20. Exercises

### Exercise A — Safe wrapper around unsafe code

Wrap one unsafe primitive inside a safe API. Write down every safety invariant and tests that exercise boundary conditions.

### Exercise B — C FFI wrapper

Create a minimal Rust wrapper around a C function. Define ownership rules for memory crossing the boundary.

### Exercise C — Allocation audit

Take a parser or transformation pipeline and measure allocations. Reduce allocations only when profiling shows a meaningful bottleneck.

### Exercise D — Data-layout experiment

Implement the same workload using a pointer-heavy structure and a contiguous representation. Benchmark both and explain the result.

## 21. Unsafe mastery standard

Before approving unsafe production code, you should be able to answer:

```text
What does the compiler normally prove here?
What proof are we taking over manually?
What is the exact invariant?
Where is the invariant established?
Can safe code violate it later?
Can the unsafe region be smaller?
How is it tested?
```

## References

- Rustonomicon: https://doc.rust-lang.org/nomicon/
- What Unsafe Can Do: https://doc.rust-lang.org/nomicon/what-unsafe-does.html
- Working with Unsafe: https://doc.rust-lang.org/nomicon/working-with-unsafe.html
- FFI module: https://doc.rust-lang.org/std/ffi/
- Rust Reference: https://doc.rust-lang.org/stable/reference/


---

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


---

# Rust Study Tracker

## How to use

Mark a box only when you can explain the concept and use it in code without copying a tutorial solution.

## Foundations

- [ ] Install Rust with rustup
- [ ] `rustc`, `cargo`, `rustup` basics
- [ ] Cargo project structure
- [ ] Variables and mutability
- [ ] Primitive types
- [ ] Functions and expressions
- [ ] Control flow
- [ ] Structs
- [ ] Enums
- [ ] `match`
- [ ] `Option`
- [ ] `Result`
- [ ] `?`
- [ ] Strings and slices
- [ ] Collections
- [ ] Modules

## Ownership

- [ ] Move semantics
- [ ] `Copy`
- [ ] `Clone`
- [ ] Shared borrowing
- [ ] Mutable borrowing
- [ ] Slice references
- [ ] Lifetime basics
- [ ] Lifetime annotations
- [ ] Struct lifetime parameters
- [ ] `Box`
- [ ] `Rc`
- [ ] `Arc`
- [ ] Interior mutability
- [ ] `mem::take`
- [ ] `mem::replace`

## Abstraction

- [ ] Generics
- [ ] Trait definitions
- [ ] Trait bounds
- [ ] `where`
- [ ] Associated types
- [ ] `dyn Trait`
- [ ] Iterator adapters
- [ ] Closure traits
- [ ] Newtypes
- [ ] Type-state pattern
- [ ] Macros basics

## Engineering

- [ ] Unit tests
- [ ] Integration tests
- [ ] Documentation tests
- [ ] Custom error types
- [ ] Cargo workspaces
- [ ] Features
- [ ] Formatting
- [ ] Clippy
- [ ] `cargo tree`
- [ ] Public API documentation
- [ ] CI pipeline

## Concurrency

- [ ] Threads
- [ ] Ownership across threads
- [ ] Channels
- [ ] `Send`
- [ ] `Sync`
- [ ] `Arc<Mutex<T>>`
- [ ] `RwLock`
- [ ] Atomics
- [ ] Memory ordering basics

## Async

- [ ] Future model
- [ ] `async fn`
- [ ] `.await`
- [ ] Executor
- [ ] Tasks
- [ ] Blocking vs async work
- [ ] Cancellation
- [ ] Backpressure
- [ ] Pinning

## Advanced

- [ ] Trait coherence
- [ ] Variance
- [ ] Higher-ranked trait bounds
- [ ] GATs
- [ ] Auto traits
- [ ] Unsafe contracts
- [ ] Raw pointers
- [ ] FFI
- [ ] `repr(C)`
- [ ] ABI boundaries
- [ ] Performance profiling
- [ ] Allocation analysis
- [ ] Zero-copy design

## Projects

- [ ] CLI calculator
- [ ] Log analyzer
- [ ] File indexer
- [ ] Config library
- [ ] Concurrent job queue
- [ ] Async pipeline
- [ ] HTTP proxy/cache
- [ ] Key-value store
- [ ] Rust/C FFI wrapper

## Final review

- [ ] I can explain ownership without examples from memory.
- [ ] I can redesign APIs to avoid unnecessary cloning.
- [ ] I can use `Result` and typed errors for expected failures.
- [ ] I can reason about `Send` and `Sync`.
- [ ] I understand the difference between async tasks and OS threads.
- [ ] I can review an unsafe block and identify its invariant.
- [ ] I can profile before optimizing.
- [ ] I can ship a crate with tests, docs, CI, and dependency discipline.
