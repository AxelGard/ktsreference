

# getDoubleAt

Gets Double out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.getDoubleAt(index: Int): Double(source)
```

```kotlin
import kotlin.native.concurrent.ExperimentalNativeApi
import kotlin.math.*

// A helper to write a Double into a ByteArray (little‑endian)
fun doubleToBytes(value: Double): ByteArray {
    val raw = java.lang.Double.doubleToRawLongBits(value)
    val bytes = ByteArray(8)
    for (i in 0 until 8) {
        bytes[i] = (raw shr (8 * i)).toByte()
    }
    return bytes
}

@ExperimentalNativeApi
fun main() {
    // Create a byte array that contains the double 42.42
    val data: ByteArray = doubleToBytes(42.42)

    // Read the double back from the byte array
    val extracted: Double = data.getDoubleAt(0)

    println("Extracted value: $extracted")   // prints: Extracted value: 42.42
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/get-double-at.html)

    