

# utf8

the value of zero-terminated UTF-8-encoded C string constructed from given kotlin.String.

```kotlin
val String.utf8: CValues<ByteVar>(source)
```

```kotlin
import kotlinx.cinterop.*

@CName("print_c_string")
external fun printCString(ptr: CPointer<ByteVar>)

fun main() {
    val message = "Hello, Kotlin!"

    // Convert the Kotlin string to a zero‑terminated UTF‑8 C string
    message.utf8.usePinned { pinned ->
        // Pass the C pointer to a C function
        printCString(pinned.addressOf(0))
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/utf8.html)

    