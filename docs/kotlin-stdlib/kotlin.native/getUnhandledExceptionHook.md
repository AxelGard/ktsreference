

# getUnhandledExceptionHook

Returns a user-defined unhandled exception hook set by setUnhandledExceptionHook or null if no user-defined hooks were set.

```kotlin
@ExperimentalNativeApifun getUnhandledExceptionHook(): ReportUnhandledExceptionHook?(source)
```

```kotlin
import kotlin.native.concurrent.*
import kotlin.native.runtime.*
import kotlin.native.*
import kotlin.native.*

@ExperimentalNativeApi
fun main() {
    // Define a custom unhandled exception hook that prints the exception
    val customHook: ReportUnhandledExceptionHook = { exception ->
        println("Unhandled exception captured: ${exception.message}")
    }

    // Register the hook
    setUnhandledExceptionHook(customHook)

    // Retrieve the hook we just set
    val retrievedHook = getUnhandledExceptionHook()

    // Verify that the hook is the same we registered
    println("Hook retrieved: ${retrievedHook != null}") // should print true

    // Throw an exception to see the hook in action
    throw IllegalStateException("Test exception")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/get-unhandled-exception-hook.html)

    