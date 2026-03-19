

# filterNot

Returns a list containing all elements not matching the given predicate.

```kotlin
inline fun <T> Array<out T>.filterNot(predicate: (T) -> Boolean): List<T>(source)
```

```kotlin
fun main() {
    val fruits = arrayOf("apple", "banana", "cherry", "blueberry", "avocado")

    // Keep only fruits that do NOT start with 'b'
    val nonBStart = fruits.filterNot { it.startsWith('b') }

    println(nonBStart) // Output: [apple, cherry, avocado]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter-not.html)

    