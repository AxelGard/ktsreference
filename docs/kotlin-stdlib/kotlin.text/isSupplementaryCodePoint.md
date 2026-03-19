

# isSupplementaryCodePoint

Checks if the codepoint specified is a supplementary codepoint or not.

```kotlin
@ExperimentalNativeApiactual fun Char.Companion.isSupplementaryCodePoint(codepoint: Int): Boolean(source)
```

```kotlin
@OptIn(ExperimentalNativeApi::class)
fun main() {
    val smiley = 0x1F600          // 😀 – a supplementary code point
    val latinA = 0x0041           // A – a basic multilingual plane code point

    println("Is 0x1F600 supplementary? ${Char.isSupplementaryCodePoint(smiley)}")
    println("Is 0x0041 supplementary? ${Char.isSupplementaryCodePoint(latinA)}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-supplementary-code-point.html)

    