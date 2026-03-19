

# wcstr

the value of zero-terminated UTF-16-encoded C string constructed from given kotlin.String.

```kotlin
val String.wcstr: CValues<UShortVar>(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.*

fun main() {
    val kotlinString = "Hello, Kotlin/Native!"

    memScoped {
        // Convert the Kotlin String to a null‑terminated UTF‑16 C wide string
        val wideString = kotlinString.wcstr

        // Obtain a native pointer that can be passed to C functions
        val ptr: CPointer<UShortVar> = wideString.getPointer(memScope)

        // Example: print the wide string with a C function that expects wchar_t*
        wprintf("%ls\n".cstr, ptr)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/wcstr.html)

    