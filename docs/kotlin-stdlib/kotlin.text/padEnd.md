

# padEnd

Returns a char sequence with content of this char sequence padded at the end to the specified length with the specified character or space.

```kotlin
fun CharSequence.padEnd(length: Int, padChar: Char = ' '): CharSequence(source)
```

```kotlin
fun main() {
    val word = "Kotlin"

    // Pad with spaces to a total length of 10
    val paddedWithSpaces = word.padEnd(10)
    println(">$paddedWithSpaces<") // prints 'Kotlin    '

    // Pad with hyphens to a total length of 10
    val paddedWithHyphens = word.padEnd(10, '-')
    println(">$paddedWithHyphens<") // prints 'Kotlin----'
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/pad-end.html)

    