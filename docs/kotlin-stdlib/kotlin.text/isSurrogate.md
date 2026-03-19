

# isSurrogate

Returns true if this character is a Unicode surrogate code unit.

```kotlin
fun Char.isSurrogate(): Boolean(source)
```

fun main() {
    val highSurrogate = '\uD83D' // high surrogate
    val lowSurrogate  = '\uDE00' // low surrogate
    val regularChar   = 'A'

    println("Is '$highSurrogate' a surrogate? ${highSurrogate.isSurrogate()}")
    println("Is '$lowSurrogate'  a surrogate? ${lowSurrogate.isSurrogate()}")
    println("Is '$regularChar'   a surrogate? ${regularChar.isSurrogate()}")
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-surrogate.html)

    