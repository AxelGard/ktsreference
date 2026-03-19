

# lazyOf

Creates a new instance of the Lazy that is already initialized with the specified value.

```kotlin
fun <T> lazyOf(value: T): Lazy<T>(source)
```

```kotlin
val precomputed: Lazy<Int> = lazyOf(100)

fun main() {
    // The value is already initialized; no lazy block is executed here.
    println(precomputed.value) // prints 100
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/lazy-of.html)

    