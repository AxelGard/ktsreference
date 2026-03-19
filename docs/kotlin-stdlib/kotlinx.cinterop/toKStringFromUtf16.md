

# toKStringFromUtf16

the kotlin.String decoded from given zero-terminated UTF-16-encoded C string.

```kotlin
fun CPointer<ShortVar>.toKStringFromUtf16(): String(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.*

fun main() = memScoped {
    // Allocate a zero‑terminated UTF‑16 C string that holds "Hello"
    val utf16Ptr = allocArray<ShortVar>(6).apply {
        this[0] = 'H'.toShort()
        this[1] = 'e'.toShort()
        this[2] = 'l'.toShort()
        this[3] = 'l'.toShort()
        this[4] = 'o'.toShort()
        this[5] = 0         // null terminator
    }

    // Convert the C string to a Kotlin String
    val kotlinString = utf16Ptr.toKStringFromUtf16()

    println(kotlinString)   // prints: Hello
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/to-k-string-from-utf16.html)

    