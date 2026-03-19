

# setUnhandledExceptionHook

Installs an unhandled exception hook and returns an old hook, or null if no user-defined hooks were previously set.

```kotlin
@ExperimentalNativeApi@IgnorableReturnValuefun setUnhandledExceptionHook(hook: ReportUnhandledExceptionHook?): ReportUnhandledExceptionHook?(source)
```

```kotlin
import kotlin.native.*

@OptIn(ExperimentalNativeApi::class)
fun main() {
    // Install a hook that logs every unhandled exception
    val oldHook = setUnhandledExceptionHook { exception, stackTrace ->
        println("Caught unhandled exception: ${exception.message}")
        // Return true to indicate the exception was handled
        true
    }

    // Trigger an unhandled exception
    val array = IntArray(1)
    println(array[10])   // IndexOutOfBoundsException
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/set-unhandled-exception-hook.html)

    