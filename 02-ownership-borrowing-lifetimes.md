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

can be written without an explicit `'a` because the input/reference-output relationship is unambiguous.

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

Reference-counted shared ownership for single-threaded code.

### `Arc<T>`

Atomically reference-counted shared ownership for multi-threaded code.

`Rc` is not thread-safe; `Arc` provides the synchronization needed for reference-count updates.

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
