

# printStackTrace

Prints the detailed description of this throwable to the standard output or standard error output.

```kotlin
expect fun Throwable.printStackTrace()(source)
```

```kotlin
fun main() {
    try {
        // This will throw an IndexOutOfBoundsException
        val list = listOf<Int>()
        println(list[1])
    } catch (e: Exception) {
        // Print the stack trace to standard error
        e.printStackTrace()
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/print-stack-trace.html)

    