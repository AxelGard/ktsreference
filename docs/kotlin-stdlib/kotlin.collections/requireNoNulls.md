

# requireNoNulls

Returns an original collection containing all the non-null elements, throwing an IllegalArgumentException if there are any null elements.

```kotlin
fun <T : Any> Array<T?>.requireNoNulls(): Array<T>(source)
```

```kotlin
fun main() {
    // Example with no nulls
    val names: Array<String?> = arrayOf("Alice", "Bob", "Charlie")
    val nonNullNames = names.requireNoNulls()
    println(nonNullNames.joinToString())

    // Example with a null element
    val numbers: Array<Int?> = arrayOf(1, 2, null, 4)
    try {
        numbers.requireNoNulls()
    } catch (e: IllegalArgumentException) {
        println("Caught exception: ${e.message}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/require-no-nulls.html)

    