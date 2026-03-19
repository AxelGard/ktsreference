

# toByteArray

Encodes the contents of this string using the specified character set and returns the resulting byte array.

```kotlin
inline fun String.toByteArray(charset: Charset = Charsets.UTF_8): ByteArray(source)
```

```kotlin
fun main() {
    val text = "Hello, Kotlin!"
    val bytes = text.toByteArray(Charsets.UTF_8)
    println(bytes.joinToString(prefix = "[", postfix = "]") { it.toString() })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-byte-array.html)

    