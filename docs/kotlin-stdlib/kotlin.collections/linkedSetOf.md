

# linkedSetOf

Returns an empty new LinkedHashSet.

```kotlin
inline fun <T> linkedSetOf(): LinkedHashSet<T>(source)
```

```kotlin
fun main() {
    // Create a LinkedHashSet with initial elements (duplicates are removed, order preserved)
    val fruits = linkedSetOf("apple", "banana", "apple", "orange")

    // Add a new element
    fruits.add("pear")

    // Remove an element
    fruits.remove("banana")

    // Iterate over the set – order is the order of first insertion
    for (fruit in fruits) {
        println(fruit)
    }

    // Create an empty LinkedHashSet
    val emptySet = linkedSetOf<Int>()
    println("Empty set size: ${emptySet.size}")  // 0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/linked-set-of.html)

    