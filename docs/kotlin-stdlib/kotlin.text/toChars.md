

# toChars

Converts the codepoint specified to a char array. If the codepoint is not supplementary, the method will return an array with one element otherwise it will return an array A with a high surrogate in A0 and a low surrogate in A1.

```kotlin
@ExperimentalNativeApiactual fun Char.Companion.toChars(codePoint: Int): CharArray(source)
```

```kotlin
fun main() {
    // Non‑supplementary code point (ASCII 'A')
    val codePointA = 0x0041
    val charsA = Char.toChars(codePointA)
    println("Code point U+${codePointA.toString(16)} -> ${charsA.joinToString("")}") // prints A

    // Supplementary code point (😀)
    val codePointSmiley = 0x1F600
    val charsSmiley = Char.toChars(codePointSmiley)
    println("Code point U+${codePointSmiley.toString(16)} -> ${charsSmiley.joinToString("")}") // prints 😀
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-chars.html)

    