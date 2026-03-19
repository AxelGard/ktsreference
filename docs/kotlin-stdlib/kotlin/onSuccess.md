

# onSuccess

Performs the given action on the encapsulated value if this instance represents success. Returns the original Result unchanged.

```kotlin
@IgnorableReturnValueinline fun <T> Result<T>.onSuccess(action: (value: T) -> Unit): Result<T>(source)
```

```kotlin
fun main() {
    val result: Result<Int> = Result.success(10)

    result
        .onSuccess { value ->
            println("Success! The value is $value")
        }
        .onFailure { exception ->
            println("Failure: ${exception.message}")
        }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/on-success.html)

    