

# none

Returns true if the sequence has no elements.

```kotlin
fun <T> Sequence<T>.none(): Boolean(source)
```

val numbers = sequenceOf(1, 2, 3)
val hasNoEven = numbers.none { it % 2 == 0 }
println(hasNoEven) // prints: false

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/none.html)

    