

# getOrDefault

Returns the encapsulated value if this instance represents success or the defaultValue if it is failure.

```kotlin
inline fun <R, T : R> Result<T>.getOrDefault(defaultValue: R): R(source)
```

```kotlin
fun main() {
    val success: Result<Int> = Result.success(10)
    val failure: Result<Int> = Result.failure(Exception("error"))

    val defaultValue = -1

    println(success.getOrDefault(defaultValue))   // prints 10
    println(failure.getOrDefault(defaultValue))  // prints -1
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/get-or-default.html)

    