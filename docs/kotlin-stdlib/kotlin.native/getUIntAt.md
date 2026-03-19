

# getUIntAt

Gets UInt out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApi@ExperimentalUnsignedTypesexternal fun ByteArray.getUIntAt(index: Int): UInt(source)
```

```kotlin
@ExperimentalNativeApi
@ExperimentalUnsignedTypes
fun main() {
    // 8-byte array: 0x01020304 0x05060708 (little‑endian)
    val data = byteArrayOf(0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08)

    // Read the first UInt (bytes 0‑3)
    val first = data.getUIntAt(0)   // 0x01020304 → 16909060

    // Read the second UInt (bytes 4‑7)
    val second = data.getUIntAt(4)  // 0x05060708 → 84281096

    println("first UInt = $first")
    println("second UInt = $second")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/get-u-int-at.html)

    