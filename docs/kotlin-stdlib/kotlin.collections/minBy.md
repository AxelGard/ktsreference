

# minBy

Returns the first element yielding the smallest value of the given selector function.

```kotlin
@JvmName(name = "minByOrThrow")inline fun <T, R : Comparable<R>> Array<out T>.minBy(selector: (T) -> R): T(source)
```

```kotlin
data class Product(val name: String, val price: Double)

val products = arrayOf(
    Product("Apple", 1.20),
    Product("Banana", 0.80),
    Product("Cherry", 2.50)
)

val cheapest = products.minBy { it.price }
println("Cheapest product: ${cheapest.name} at \$${cheapest.price}")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/min-by.html)

    