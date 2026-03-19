

# shuffled

Returns a new list with the elements of this list randomly shuffled using the specified random instance as the source of randomness.

```kotlin
fun <T> Iterable<T>.shuffled(random: Random): List<T>(source)
```

```kotlin
import kotlin.random.Random

fun main() {
    val items = listOf("apple", "banana", "cherry", "date")
    val random = Random(12345)
    val shuffledItems = items.shuffled(random)
    
    println("Original: $items")
    println("Shuffled: $shuffledItems")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/shuffled.html)

    