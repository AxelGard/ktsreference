

# takeLast

Returns a list containing last n elements.

```kotlin
fun <T> Array<out T>.takeLast(n: Int): List<T>(source)
```

```kotlin
fun main() {
    val fruits = arrayOf("Apple", "Banana", "Cherry", "Date", "Elderberry")
    val lastTwo = fruits.takeLast(2)
    println(lastTwo) // Output: [Date, Elderberry]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/take-last.html)

    