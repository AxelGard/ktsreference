

# getOrThrow

Returns the encapsulated value if this instance represents success or throws the encapsulated Throwable exception if it is failure.

```kotlin
inline fun <T> Result<T>.getOrThrow(): T(source)
```

```kotlin
import kotlin.Result

fun main() {
    // Success case
    val success: Result<Int> = Result.success(42)
    val value = success.getOrThrow()   // value = 42
    println("Success value: $value")

    // Failure case
    val failure: Result<Int> = Result.failure(RuntimeException("Something went wrong"))
    try {
        failure.getOrThrow()
    } catch (e: Throwable) {
        println("Caught exception: ${e.message}")   // prints: Something went wrong
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/get-or-throw.html)

    