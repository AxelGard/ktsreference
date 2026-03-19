

# isSurrogatePair

Checks if the specified high and low chars are Char.isHighSurrogate and Char.isLowSurrogate correspondingly.

```kotlin
@ExperimentalNativeApiactual fun Char.Companion.isSurrogatePair(high: Char, low: Char): Boolean(source)
```

```kotlin
import kotlin.text.Char

fun main() {
    val high = '\uD83D'   // high surrogate for 😀
    val low  = '\uDE00'   // low surrogate for 😀

    val isPair = Char.isSurrogatePair(high, low)

    println("Is the pair a surrogate pair? $isPair") // true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-surrogate-pair.html)

    