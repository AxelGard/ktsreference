

# maxOfOrNull

Returns the largest value among all values produced by selector function applied to each element in the sequence or null if the sequence is empty.

```kotlin
inline fun <T> Sequence<T>.maxOfOrNull(selector: (T) -> Double): Double?(source)
```

```kotlin
data class Item(val id: Int, val weight: Double)

fun main() {
    val items = listOf(
        Item(1, 2.5),
        Item(2, 5.0),
        Item(3, 3.2)
    ).asSequence()

    val maxWeight = items.maxOfOrNull { it.weight }
    println("Maximum weight: $maxWeight")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/max-of-or-null.html)

    