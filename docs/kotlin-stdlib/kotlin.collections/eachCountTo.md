

# eachCountTo

Groups elements from the Grouping source by key and counts elements in each group to the given destination map.

```kotlin
fun <T, K, M : MutableMap<in K, Int>> Grouping<T, K>.eachCountTo(destination: M): M(source)
```

```kotlin
fun main() {
    val words = listOf("apple", "banana", "apricot", "blueberry", "avocado")
    val countMap = mutableMapOf<Char, Int>()

    words.groupingBy { it.first() }.eachCountTo(countMap)

    println(countMap)  // Output: {a=3, b=2}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/each-count-to.html)

    