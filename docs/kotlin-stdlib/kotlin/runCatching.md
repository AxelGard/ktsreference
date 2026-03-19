

# runCatching

Calls the specified function block and returns its encapsulated result if invocation was successful, catching any Throwable exception that was thrown from the block function execution and encapsulating it as a failure.

```kotlin
inline fun <R> runCatching(block: () -> R): Result<R>(source)
```

```kotlin
fun main() {
    val result = runCatching { riskyOperation() }

    result.onSuccess { value ->
        println("Success! Result: $value")
    }.onFailure { exception ->
        println("Failed with exception: ${exception.message}")
    }
}

fun riskyOperation(): Int {
    // Intentionally throw an exception for demo purposes
    return 10 / 0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/run-catching.html)

    