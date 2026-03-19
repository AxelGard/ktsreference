

# callContinuation2

This API is deprecated without replacement

```kotlin
fun <T1, T2> COpaquePointer.callContinuation2()(source)
```

```kotlin
import kotlin.native.concurrent.*
import kotlin.native.internal.*

// Simulated function that receives a COpaquePointer to a suspended continuation
fun resumeSuspendedContinuation(ptr: COpaquePointer) {
    // Resume the continuation with two results
    ptr.callContinuation2("Success", 200)
}

fun main() {
    // Imagine we obtained a COpaquePointer to a continuation from some native interop code
    val continuationPtr: COpaquePointer = obtainContinuationPointer()

    // Resume that continuation with two values
    resumeSuspendedContinuation(continuationPtr)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native.concurrent/call-continuation2.html)

    