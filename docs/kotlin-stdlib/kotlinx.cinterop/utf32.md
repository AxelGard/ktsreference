

# utf32

the value of zero-terminated UTF-32-encoded C string constructed from given kotlin.String.

```kotlin
val String.utf32: CValues<IntVar>(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.*

@CName("print_utf32")
external fun print_utf32(str: CPointer<IntVar>)

fun main() {
    val myText = "Hello, Kotlin 🌍"
    myText.utf32.use { utf32Ptr ->
        // utf32Ptr is a CPointer<IntVar> pointing to a null‑terminated UTF‑32 string
        print_utf32(utf32Ptr)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/utf32.html)

    