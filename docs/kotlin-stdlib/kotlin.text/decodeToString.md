

# decodeToString

Decodes a string from the bytes in UTF-8 encoding in this array.

```kotlin
expect fun ByteArray.decodeToString(): String(source)
```

```kotlin
val utf8Bytes = "Kotlin 🚀".toByteArray(Charsets.UTF_8)
val decodedString = utf8Bytes.decodeToString()
println(decodedString)  // Output: Kotlin 🚀
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/decode-to-string.html)

    