

# cValuesOf

Returns sequence of immutable values CValues to pass them to C code.

```kotlin
fun cValuesOf(vararg elements: Byte): CValues<ByteVar>(source)
```

```kotlin
import kotlinx.cinterop.*

@CName("processBytes")
external fun processBytes(data: CValues<ByteVar>, length: Int)

fun main() {
    val bytes = cValuesOf(0x41.toByte(), 0x42.toByte(), 0x43.toByte()) // "ABC"
    processBytes(bytes, bytes.size)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/c-values-of.html)

    