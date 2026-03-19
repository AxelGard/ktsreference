

# distinct

Returns a list containing only distinct elements from the given array.

```kotlin
fun <T> Array<out T>.distinct(): List<T>(source)
```

```kotlin
fun main() {
    val items = arrayOf("apple", "banana", "apple", "orange", "banana")
    val unique = items.distinct()
    println(unique)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/distinct.html)

    