

# map

Returns the encapsulated result of the given transform function applied to the encapsulated value if this instance represents success or the original encapsulated Throwable exception if it is failure.

```kotlin
inline fun <R, T> Result<T>.map(transform: (value: T) -> R): Result<R>(source)
```

```kotlin
fun main() {
    // Success case
    val successResult: Result<Int> = Result.success(10)
    val mappedSuccess = successResult.map { it * 2 }
    println(mappedSuccess)   // Result.success(20)

    // Failure case
    val failureResult: Result<Int> = Result.failure(Exception("Oops"))
    val mappedFailure = failureResult.map { it * 2 }
    println(mappedFailure)   // Result.failure(java.lang.Exception: Oops)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/map.html)

    