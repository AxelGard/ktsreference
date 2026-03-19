

# utf16

the value of zero-terminated UTF-16-encoded C string constructed from given kotlin.String.

```kotlin
val String.utf16: CValues<UShortVar>(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.wcslen

fun main() {
    val kotlinString = "Hello, 世界"
    val utf16 = kotlinString.utf16
    utf16.useContents { ptr ->
        val len = wcslen(ptr)
        println("UTF‑16 length: $len")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/utf16.html)

    