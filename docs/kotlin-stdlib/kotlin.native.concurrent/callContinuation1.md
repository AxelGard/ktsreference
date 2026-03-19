

# callContinuation1

This API is deprecated without replacement

```kotlin
fun <T1> COpaquePointer.callContinuation1()(source)
```

```kotlin
import kotlinx.cinterop.*
import kotlin.native.concurrent.*

fun main() {
    // Create a single‑threaded context
    val thread = newSingleThreadContext("myThread")

    // Create a continuation that will print its result when resumed
    val cont: Continuation<Int> = thread.newContinuation { value ->
        println("Continuation resumed with $value")
    }

    // Pass the continuation to C code as a COpaquePointer
    val ptr = cont as COpaquePointer

    // Simulate a C callback that receives the pointer and resumes the continuation
    fun cCallback(p: COpaquePointer) {
        // Resume the continuation with the value 42
        p.callContinuation1(42)
    }

    // Invoke the simulated C callback
    cCallback(ptr)
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native.concurrent/call-continuation1.html)

    