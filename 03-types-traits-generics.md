# 03 — Types, Traits, Generics, and Zero-Cost Abstractions

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
- Advanced types: https://doc.rust-lang.org/book/ch20-02-advanced-types.html
- Rust Reference: https://doc.rust-lang.org/stable/reference/
