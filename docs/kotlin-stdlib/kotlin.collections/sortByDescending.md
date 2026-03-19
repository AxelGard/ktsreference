

# sortByDescending

Sorts elements in the array in-place descending according to natural sort order of the value returned by specified selector function.

```kotlin
inline fun <T, R : Comparable<R>> Array<out T>.sortByDescending(crossinline selector: (T) -> R?)(source)
```

```kotlin
data class Product(val name: String, val price: Double)

fun main() {
    val products = arrayOf(
        Product("Apple", 1.99),
        Product("Banana", 0.99),
        Product("Cherry", 2.49)
    )

    // Sort products in-place by price in descending order
    products.sortByDescending { it.price }

    println(products.joinToString { "${it.name}: \$${it.price}" })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sort-by-descending.html)

    