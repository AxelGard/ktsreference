

# maxOfWith

Returns the largest value according to the provided comparator among all values produced by selector function applied to each element in the sequence.

```kotlin
inline fun <T, R> Sequence<T>.maxOfWith(comparator: Comparator<in R>, selector: (T) -> R): R(source)
```

```kotlin
data class Product(val name: String, val price: Double)

fun main() {
    val products = listOf(
        Product("Apple", 0.99),
        Product("Banana", 1.49),
        Product("Cherry", 2.99)
    ).asSequence()

    val mostExpensive = products.maxOfWith(
        compareBy<Product> { it.price }, // comparator for the selected value
        { it }                           // selector that returns the product itself
    )

    println("Most expensive: ${mostExpensive.name} at \$${mostExpensive.price}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/max-of-with.html)

    