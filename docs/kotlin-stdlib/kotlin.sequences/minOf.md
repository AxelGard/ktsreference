

# minOf

Returns the smallest value among all values produced by selector function applied to each element in the sequence.

```kotlin
inline fun <T> Sequence<T>.minOf(selector: (T) -> Double): Double(source)
```

```kotlin
data class Product(val name: String, val price: Double)

fun main() {
    val products = listOf(
        Product("Apple", 1.99),
        Product("Banana", 0.99),
        Product("Cherry", 2.49)
    ).asSequence()

    val cheapestPrice = products.minOf { it.price }
    println("Cheapest price: $cheapestPrice")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/min-of.html)

    