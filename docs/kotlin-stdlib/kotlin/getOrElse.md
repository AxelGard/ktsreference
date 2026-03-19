

# getOrElse

Returns the encapsulated value if this instance represents success or the result of onFailure function for the encapsulated Throwable exception if it is failure.

```kotlin
inline fun <R, T : R> Result<T>.getOrElse(onFailure: (exception: Throwable) -> R): R(source)
```

```kotlin
fun main() {
    // Example with a successful Result
    val success: Result<Int> = Result.success(42)
    val successValue = success.getOrElse { /* this block won't be executed */ 0 }
    println("Success value: $successValue") // prints: Success value: 42

    // Example with a failing Result
    val failure: Result<Int> = runCatching { 10 / 0 }   // throws ArithmeticException
    val fallbackValue = failure.getOrElse { e ->
        println("Caught exception: ${e.message}")
        -1
    }
    println("Fallback value: $fallbackValue") // prints: Fallback value: -1
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/get-or-else.html)

    