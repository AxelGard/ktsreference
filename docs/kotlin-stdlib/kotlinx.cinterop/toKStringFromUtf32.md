

# toKStringFromUtf32

the kotlin.String decoded from given zero-terminated UTF-32-encoded C string.

```kotlin
fun CPointer<IntVar>.toKStringFromUtf32(): String(source)
```

```kotlin
import kotlinx.cinterop.*

fun main() = memScoped {
    // Allocate a UTF‑32 null‑terminated string: "Hello"
    val utf32Ptr = allocArray<IntVar>(6)
    utf32Ptr[0] = 'H'.code          // U+0048
    utf32Ptr[1] = 'e'.code          // U+0065
    utf32Ptr[2] = 'l'.code          // U+006C
    utf32Ptr[3] = 'l'.code          // U+006C
    utf32Ptr[4] = 'o'.code          // U+006F
    utf32Ptr[5] = 0                 // null terminator

    // Convert the UTF‑32 C string to a Kotlin String
    val kotlinString: String = utf32Ptr.toKStringFromUtf32()

    println(kotlinString) // prints: Hello
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/to-k-string-from-utf32.html)

    