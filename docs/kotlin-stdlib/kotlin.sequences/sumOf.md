

# sumOf

Returns the sum of all values produced by selector function applied to each element in the sequence.

```kotlin
@JvmName(name = "sumOfDouble")inline fun <T> Sequence<T>.sumOf(selector: (T) -> Double): Double(source)
```

```kotlin
data class Item(val price: Double)

fun main() {
    val items = sequenceOf(
        Item(10.0),
        Item(20.5),
        Item(5.25)
    )

    val totalPrice: Double = items.sumOf { it.price }

    println("Total price: $totalPrice") // Output: Total price: 35.75
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/sum-of.html)

    