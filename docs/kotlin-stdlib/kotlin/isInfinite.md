

# isInfinite

Returns true if this value is infinitely large in magnitude.

```kotlin
expect fun Double.isInfinite(): Boolean(source)
```

```kotlin
fun main() {
    val posInf = Double.POSITIVE_INFINITY
    val negInf = Double.NEGATIVE_INFINITY
    val finite = 42.0

    println("Is $posInf infinite? ${posInf.isInfinite()}")
    println("Is $negInf infinite? ${negInf.isInfinite()}")
    println("Is $finite infinite? ${finite.isInfinite()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/is-infinite.html)

    