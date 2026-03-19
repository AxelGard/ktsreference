

# firstNotNullOfOrNull

Returns the first non-null value produced by transform function being applied to elements of this sequence in iteration order, or null if no non-null value was produced.

```kotlin
inline fun <T, R : Any> Sequence<T>.firstNotNullOfOrNull(transform: (T) -> R?): R?(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1, 2, 3, 4, 5)

    val firstEvenSquare = numbers.firstNotNullOfOrNull { number ->
        if (number % 2 == 0) number * number else null
    }

    println(firstEvenSquare) // prints: 4
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/first-not-null-of-or-null.html)

    