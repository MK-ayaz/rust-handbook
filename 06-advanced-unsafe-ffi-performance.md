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
