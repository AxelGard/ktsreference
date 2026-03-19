

# toByteOrNull

Parses the string to a Byte number or returns null if the string is not a valid representation of a Byte.

```kotlin
fun String.toByteOrNull(): Byte?(source)
```

```kotlin
fun main() {
    val input1 = "100"
    val byte1 = input1.toByteOrNull()
    println("input1: $input1 -> $byte1")   // output: input1: 100 -> 100

    val input2 = "not a number"
    val byte2 = input2.toByteOrNull()
    println("input2: $input2 -> $byte2")   // output: input2: not a number -> null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-byte-or-null.html)

    