

# hashSetOf

Returns an empty new HashSet.

```kotlin
inline fun <T> hashSetOf(): HashSet<T>(source)
```

```kotlin
fun main() {
    // Create a HashSet with initial elements
    val fruits = hashSetOf("apple", "banana", "cherry")

    // Add another element
    fruits.add("date")

    // Print the contents
    println(fruits) // [apple, banana, cherry, date]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/hash-set-of.html)

    