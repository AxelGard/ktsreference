

# minus

Returns a list containing all elements of the original collection without the first occurrence of the given element.

```kotlin
operator fun <T> Iterable<T>.minus(element: T): List<T>(source)
```

```kotlin
fun main() {
    val fruits = listOf("apple", "banana", "cherry", "banana")
    val withoutFirstBanana = fruits - "banana"

    println(withoutFirstBanana) // [apple, cherry, banana]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/minus.html)

    