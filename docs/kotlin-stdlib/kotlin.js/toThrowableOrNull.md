

# toThrowableOrNull

For a Dynamic value caught in JS, returns the corresponding Throwable if it was thrown from Kotlin, or null otherwise.

```kotlin
@ExperimentalWasmJsInteropfun JsAny.toThrowableOrNull(): Throwable?(source)
```

```kotlin
import kotlin.js.*
import kotlin.experimental.ExperimentalWasmJsInterop

@OptIn(ExperimentalWasmJsInterop::class)
class KotlinError(message: String) : RuntimeException(message)

fun throwKotlinError() {
    throw KotlinError("Something went wrong in Kotlin")
}

fun main() {
    try {
        throwKotlinError()
    } catch (e: dynamic) {          // JS exception caught as a dynamic value
        val kotlinThrowable = e.toThrowableOrNull()
        if (kotlinThrowable != null) {
            console.log("Caught Kotlin exception: ${kotlinThrowable.message}")
        } else {
            console.log("Caught a non‑Kotlin exception")
        }
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/to-throwable-or-null.html)

    