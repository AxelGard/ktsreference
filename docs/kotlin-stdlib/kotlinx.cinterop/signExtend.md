

# signExtend

Deprecated without replacement as part of the obsolete interop API

```kotlin
inline external fun <R : Number> Number.signExtend(): R(source)
```

```kotlin
import kotlinx.cinterop.signExtend

fun main() {
    // Example: convert an unsigned byte (UByte) to a signed int (Int)
    val ubyte: UByte = 0xF0u          // 240 in decimal
    val signedInt: Int = ubyte.signExtend<Int>()  // -16 after sign‑extension
    println("Signed int value: $signedInt")

    // Example: sign‑extend a signed short to a signed long
    val shortVal: Short = 0x8000.toShort()  // -32768 in 16‑bit two's‑complement
    val signedLong: Long = shortVal.signExtend<Long>() // -32768 in 64‑bit
    println("Signed long value: $signedLong")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/sign-extend.html)

    