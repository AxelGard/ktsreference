

# setULongAt

Sets ULong out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApi@ExperimentalUnsignedTypesexternal fun ByteArray.setULongAt(index: Int, value: ULong)(source)
```

```kotlin
@OptIn(ExperimentalNativeApi::class, ExperimentalUnsignedTypes::class)
fun main() {
    val buffer = ByteArray(8)          // create a byte buffer of size 8
    buffer.setULongAt(0, 0x1122334455667788uL) // write a ULong value at index 0
    // buffer now holds the 8‑byte little‑endian representation of the ULong
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/set-u-long-at.html)

    