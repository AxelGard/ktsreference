

# digitToChar

Returns the Char that represents this decimal digit. Throws an exception if this value is not in the range 0..9.

```kotlin
fun Int.digitToChar(): Char(source)
```

```kotlin
fun main() {
    val digit = 7
    val char = digit.digitToChar()
    println(char) // prints: 7
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/digit-to-char.html)

    