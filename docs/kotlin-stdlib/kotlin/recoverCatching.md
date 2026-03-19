

# recoverCatching

Returns the encapsulated result of the given transform function applied to the encapsulated Throwable exception if this instance represents failure or the original encapsulated value if it is success.

```kotlin
inline fun <R, T : R> Result<T>.recoverCatching(transform: (exception: Throwable) -> R): Result<R>(source)
```

```kotlin
import kotlin.runCatching

fun main() {
    // Successful parsing
    val success = runCatching { "42".toInt() }                 // Result<Int>
    val recoveredSuccess = success.recoverCatching { e -> 0 }   // Result<Number>
    println(recoveredSuccess.getOrThrow()) // prints 42

    // Failed parsing, recover to a default value
    val failure = runCatching { "not a number".toInt() }       // Result<Int>
    val recoveredFailure = failure.recoverCatching { e -> 0 }  // Result<Number>
    println(recoveredFailure.getOrThrow()) // prints 0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/recover-catching.html)

    