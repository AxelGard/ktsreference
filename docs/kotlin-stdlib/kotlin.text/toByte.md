

# toByte

Parses the string to a Byte number.

```kotlin
expect fun String.toByte(): Byte(source)
```

fun main() {
    val numberString = "42"
    val byteValue: Byte = numberString.toByte()
    println(byteValue) // prints 42
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-byte.html)

    