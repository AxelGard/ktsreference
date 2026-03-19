

# cstr

the value of zero-terminated UTF-8-encoded C string constructed from given kotlin.String.

```kotlin
val String.cstr: CValues<ByteVar>(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.*

fun main() {
    val kotlinStr = "Hello, Kotlin/Native!"
    val cStr = kotlinStr.cstr

    // Example: get length using strlen
    val len = strlen(cStr.get())
    println("C string length: $len")

    // Example: print using printf
    printf("%s\n", cStr.get())
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/cstr.html)

    