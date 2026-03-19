

# toKStringFromUtf8

the kotlin.String decoded from given zero-terminated UTF-8-encoded C string.

```kotlin
fun CPointer<ByteVar>.toKStringFromUtf8(): String(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.free
import platform.posix.strdup

fun main() = memScoped {
    // Obtain a C string pointer (UTF‑8 encoded, zero‑terminated)
    val cStr: CPointer<ByteVar> = strdup("Hello, C string!")!!

    // Convert the C string to a Kotlin String
    val kotlinString = cStr.toKStringFromUtf8()

    println(kotlinString)   // prints: Hello, C string!

    // Clean up the allocated C string
    free(cStr)
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/to-k-string-from-utf8.html)

    