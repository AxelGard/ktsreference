

# onFailure

Performs the given action on the encapsulated Throwable exception if this instance represents failure. Returns the original Result unchanged.

```kotlin
@IgnorableReturnValueinline fun <T> Result<T>.onFailure(action: (exception: Throwable) -> Unit): Result<T>(source)
```

```kotlin
fun riskyOperation(): Result<Int> =
    runCatching { 10 / 0 }   // will throw ArithmeticException

fun main() {
    riskyOperation()
        .onFailure { e ->
            // This block runs only when the Result is a failure
            println("Operation failed with: ${e::class.simpleName} – ${e.message}")
        }

    // The original Result is unchanged; you can still check its status
    if (riskyOperation().isSuccess) {
        println("Result: ${riskyOperation().getOrThrow()}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/on-failure.html)

    