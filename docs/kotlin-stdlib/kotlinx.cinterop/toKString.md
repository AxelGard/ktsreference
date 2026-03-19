

# toKString

the kotlin.String decoded from given zero-terminated UTF-8-encoded C string.

```kotlin
fun CPointer<ByteVar>.toKString(): String(source)
```

```kotlin
import kotlinx.cinterop.*

fun main() {
    // Create a C string from a Kotlin string
    val cString: CPointer<ByteVar> = "Kotlin".cstr.ptr

    // Convert the C string back to a Kotlin String
    val kotlinString: String = cString.toKString()

    println(kotlinString)   // prints "Kotlin"
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/to-k-string.html)

    