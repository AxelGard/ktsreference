

# addSuppressed

 [kotlin-stdlib](/kotlin-stdlib) / [kotlin](/kotlin-stdlib/kotlin) / [addSuppressed](kotlin-stdlib/kotlin/addSuppressed)

When supported by the platform, adds the specified exception to the list of exceptions that were suppressed in order to deliver this exception.

```kotlin
expect fun Throwable.addSuppressed(exception: Throwable)(source)
```

```kotlin
fun main() {
    try {
        // Primary operation that fails
        throw IllegalArgumentException("Primary exception")
    } catch (primary: IllegalArgumentException) {
        try {
            // Secondary operation that also fails
            throw IllegalStateException("Suppressed exception")
        } catch (suppressed: IllegalStateException) {
            // Add the suppressed exception to the primary one
            primary.addSuppressed(suppressed)
        }
        // Print the stack trace to see the suppressed exception
        primary.printStackTrace()
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/add-suppressed.html)

    