

# fold

Returns the result of onSuccess for the encapsulated value if this instance represents success or the result of onFailure function for the encapsulated Throwable exception if it is failure.

```kotlin
inline fun <R, T> Result<T>.fold(onSuccess: (value: T) -> R, onFailure: (exception: Throwable) -> R): R(source)
```

```kotlin
fun main() {
    // Try to parse an integer, catching any exception
    val result: Result<Int> = runCatching { "abc".toInt() }

    // Use fold to handle success and failure in one place
    val message = result.fold(
        onSuccess = { value -> "Parsed value: $value" },
        onFailure = { exception -> "Error: ${exception.message}" }
    )

    println(message)  // Prints: Error: For input string: "abc"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/fold.html)

    