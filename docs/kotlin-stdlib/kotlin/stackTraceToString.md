

# stackTraceToString

Returns the detailed description of this throwable with its stack trace.

```kotlin
expect fun Throwable.stackTraceToString(): String(source)
```

```kotlin
fun main() {
    try {
        // Simulate an error
        val list = listOf(1, 2, 3)
        println(list[5]) // IndexOutOfBoundsException
    } catch (e: Exception) {
        println(e.stackTraceToString())
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/stack-trace-to-string.html)

    