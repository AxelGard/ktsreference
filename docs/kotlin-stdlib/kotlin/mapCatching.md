

# mapCatching

Returns the encapsulated result of the given transform function applied to the encapsulated value if this instance represents success or the original encapsulated Throwable exception if it is failure.

```kotlin
inline fun <R, T> Result<T>.mapCatching(transform: (value: T) -> R): Result<R>(source)
```

```kotlin
fun divide(a: Int, b: Int): Result<Int> =
    try {
        Result.success(a / b)
    } catch (e: Exception) {
        Result.failure(e)
    }

fun main() {
    val successResult = divide(10, 2).mapCatching { it * 2 }
    val failureResult = divide(10, 0).mapCatching { it * 2 }

    println(successResult)  // Result.success(10)
    println(failureResult)  // Result.failure(java.lang.ArithmeticException: / by zero)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/map-catching.html)

    