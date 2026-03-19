

# recover

Returns the encapsulated result of the given transform function applied to the encapsulated Throwable exception if this instance represents failure or the original encapsulated value if it is success.

```kotlin
inline fun <R, T : R> Result<T>.recover(transform: (exception: Throwable) -> R): Result<R>(source)
```

```kotlin
import kotlin.Result

fun main() {
    // A Result that represents a failure (division by zero)
    val failed: Result<Int> = Result.failure(ArithmeticException("Division by zero"))

    // Recover from the failure by providing a default value
    val recovered: Result<Int> = failed.recover { e ->
        // `e` is the Throwable that caused the failure
        if (e is ArithmeticException) 0 else -1
    }

    // Print the value: will print 0
    println(recovered.getOrElse { it })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/recover.html)

    