

# minOfOrNull

Returns the smallest value among all values produced by selector function applied to each element in the array or null if the array is empty.

```kotlin
inline fun <T> Array<out T>.minOfOrNull(selector: (T) -> Double): Double?(source)
```

```kotlin
data class Product(val name: String, val price: Double)

fun main() {
    val products = arrayOf(
        Product("Apple", 1.99),
        Product("Banana", 0.99),
        Product("Cherry", 2.49)
    )

    val cheapestPrice = products.minOfOrNull { it.price }
    println("Cheapest price: $cheapestPrice")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/min-of-or-null.html)

    