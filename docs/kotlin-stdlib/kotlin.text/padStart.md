

# padStart

Returns a char sequence with content of this char sequence padded at the beginning to the specified length with the specified character or space.

```kotlin
fun CharSequence.padStart(length: Int, padChar: Char = ' '): CharSequence(source)
```

```kotlin
fun main() {
    val paddedWithZeroes = "42".padStart(5, '0')
    val paddedWithSpaces = "42".padStart(5)

    println(paddedWithZeroes)   // 00042
    println(paddedWithSpaces)   //   42
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/pad-start.html)

    