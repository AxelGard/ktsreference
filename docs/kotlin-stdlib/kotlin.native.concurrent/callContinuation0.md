

# callContinuation0

This API is deprecated without replacement

```kotlin
fun COpaquePointer.callContinuation0()(source)
```

```kotlin
import kotlinx.cinterop.*
import kotlin.native.concurrent.*

// A suspend function that waits for a native event.
suspend fun waitForEvent(): Unit = suspendCoroutine { cont ->
    // Convert the Kotlin continuation to a C opaque pointer.
    val ptr = cont.asCPointer()

    // Pass the pointer to the native side.
    // The native code will eventually call `ptr.callContinuation0()` to resume the coroutine.
    registerCallback(ptr)
}

// A dummy native‑side implementation that immediately triggers the callback.
fun registerCallback(ptr: COpaquePointer) {
    // In real code this would be an asynchronous C call.
    // Here we just resume the coroutine immediately.
    ptr.callContinuation0()   // resumes the Kotlin coroutine
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native.concurrent/call-continuation0.html)

    