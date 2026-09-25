# 01 — Rust Fundamentals

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
