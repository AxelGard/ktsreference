

# elementAtOrNull

Returns an element at the given index or null if the index is out of bounds of this array.

```kotlin
inline fun <T> Array<out T>.elementAtOrNull(index: Int): T?(source)
```

```kotlin
fun main() {
    val fruits = arrayOf("Apple", "Banana", "Cherry")

    // Valid index
    val second = fruits.elementAtOrNull(1)   // "Banana"
    println("Element at index 1: $second")

    // Out‑of‑bounds index
    val outOfBounds = fruits.elementAtOrNull(5)   // null
    println("Element at index 5: $outOfBounds")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/element-at-or-null.html)

    