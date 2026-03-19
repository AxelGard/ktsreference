

# addSuppressed

When supported by the platform, adds the specified exception to the list of exceptions that were suppressed in order to deliver this exception.

```kotlin
expect fun Throwable.addSuppressed(exception: Throwable)(source)
```

```kotlin
fun main() {
    val primary = RuntimeException("Primary exception")
    val suppressed = RuntimeException("Suppressed exception")

    try {
        // Something that throws the primary exception
        throw primary
    } catch (e: Throwable) {
        // Add the suppressed exception
        e.addSuppressed(suppressed)
        // Re‑throw so the stack trace contains both
        throw e
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/add-suppressed.html)

    