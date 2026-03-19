

# byteArrayOf

Returns an array containing the specified Byte numbers.

```kotlin
expect fun byteArrayOf(vararg elements: Byte): ByteArray(source)
```

```kotlin
fun main() {
    val bytes = byteArrayOf(0x01, 0x02, 0x03, 0x04)
    println(bytes.joinToString(prefix = "[", postfix = "]") { "0x%02X".format(it) })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/byte-array-of.html)

    