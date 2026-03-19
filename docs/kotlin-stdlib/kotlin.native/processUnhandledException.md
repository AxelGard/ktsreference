

# processUnhandledException

Performs the default processing of unhandled exception.

```kotlin
@ExperimentalNativeApiexternal fun processUnhandledException(throwable: Throwable)(source)
```

```kotlin
import kotlin.native.processUnhandledException
import kotlin.native.ExperimentalNativeApi

@OptIn(ExperimentalNativeApi::class)
fun main() {
    try {
        // Example code that throws an exception
        throw IllegalArgumentException("Something went wrong")
    } catch (t: Throwable) {
        // Let Kotlin/Native perform its default processing of the unhandled exception
        processUnhandledException(t)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/process-unhandled-exception.html)

    