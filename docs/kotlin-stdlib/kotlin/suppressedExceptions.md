

# suppressedExceptions

Returns a list of all exceptions that were suppressed in order to deliver this exception.

```kotlin
expect val Throwable.suppressedExceptions: List<Throwable>(source)
```

```kotlin
import java.lang.Exception

class Resource : AutoCloseable {
    override fun close() {
        // This exception will be suppressed
        throw RuntimeException("close exception")
    }
}

fun main() {
    try {
        Resource().use {
            // This exception will be the primary one
            throw RuntimeException("main exception")
        }
    } catch (e: Exception) {
        println("Caught: ${e.message}")
        e.suppressedExceptions.forEach { suppressed ->
            println("Suppressed: ${suppressed.message}")
        }
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/suppressed-exceptions.html)

    