

# addSuppressed

When supported by the platform, adds the specified exception to the list of exceptions that were suppressed in order to deliver this exception.

```kotlin
expect fun Throwable.addSuppressed(exception: Throwable)(source)
```

```kotlin
import java.io.IOException

fun main() {
    try {
        // Primary failure
        throw IOException("Failed to open file")
    } catch (primary: IOException) {
        try {
            // Secondary failure during cleanup
            throw IllegalStateException("Cleanup failed")
        } catch (secondary: Exception) {
            // Suppress the secondary exception
            primary.addSuppressed(secondary)
        }
        // Rethrow the original exception with suppressed info
        throw primary
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/add-suppressed.html)

    