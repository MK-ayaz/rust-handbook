# 05 — Concurrency and Async Rust

## 1. Two different problems

**Concurrency** asks how multiple computations can make progress together.

**Parallelism** asks how computations can physically execute at the same time on multiple CPU cores.

**Async programming** is a cooperative concurrency model where tasks yield so an executor can run other tasks.

Rust supports all of these, but the ownership/type system constrains how data can cross boundaries.

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
