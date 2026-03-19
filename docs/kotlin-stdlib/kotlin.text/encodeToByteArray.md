

# encodeToByteArray

Encodes this string to an array of bytes in UTF-8 encoding.

```kotlin
expect fun String.encodeToByteArray(): ByteArray(source)
```

```kotlin
val text = "Hello, Kotlin!"
val bytes = text.encodeToByteArray()

println("Byte array: ${bytes.joinToString(", ") { it.toString() }}")

// If you need to convert it back to a String
val decoded = bytes.toString(Charsets.UTF_8)
println("Decoded string: $decoded")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/encode-to-byte-array.html)

    