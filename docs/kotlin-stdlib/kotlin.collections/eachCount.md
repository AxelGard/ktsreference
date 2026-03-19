

# eachCount

Groups elements from the Grouping source by key and counts elements in each group.

```kotlin
expect fun <T, K> Grouping<T, K>.eachCount(): Map<K, Int>(source)
```

```kotlin
fun main() {
    val fruits = listOf("apple", "apricot", "banana", "blueberry", "avocado")
    val countByFirstLetter = fruits.groupingBy { it.first() }.eachCount()
    println(countByFirstLetter) // Output: {a=3, b=2}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/each-count.html)

    