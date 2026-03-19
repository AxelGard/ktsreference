

# byteArrayOf

Returns an array containing the specified Byte numbers.

```kotlin
expect fun byteArrayOf(vararg elements: Byte): ByteArray(source)
```

```kotlin
val numbers = byteArrayOf(0x01, 0x02, 0x03, 0x04)

println(numbers.joinToString(prefix = "[", postfix = "]") { it.toString() })
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/byte-array-of.html)

    