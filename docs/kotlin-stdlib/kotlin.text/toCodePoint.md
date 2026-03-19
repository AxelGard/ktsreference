

# toCodePoint

Converts a surrogate pair to a unicode code point. Doesn't validate that the characters are a valid surrogate pair.

```kotlin
@ExperimentalNativeApiactual fun Char.Companion.toCodePoint(high: Char, low: Char): Int(source)
```

```kotlin
@OptIn(ExperimentalNativeApi::class)
fun main() {
    val high = '\uD83D' // high surrogate of 😀
    val low  = '\uDE00' // low surrogate of 😀

    val codePoint = Char.toCodePoint(high, low)
    println("Code point: U+${codePoint.toString(16).uppercase()}")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-code-point.html)

    