

# getOrNull

Returns an element at the given index or null if the index is out of bounds of this array.

```kotlin
fun <T> Array<out T>.getOrNull(index: Int): T?(source)
```

```kotlin
fun main() {
    val fruits = arrayOf("apple", "banana", "cherry")

    // Valid index
    val secondFruit = fruits.getOrNull(1)
    println(secondFruit)            // prints "banana"

    // Out-of-bounds index
    val invalidFruit = fruits.getOrNull(5)
    println(invalidFruit)           // prints "null"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/get-or-null.html)

    