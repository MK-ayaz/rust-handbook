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
