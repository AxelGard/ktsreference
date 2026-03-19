

# drop

Returns a list containing all elements except first n elements.

```kotlin
fun <T> Array<out T>.drop(n: Int): List<T>(source)
```

```kotlin
fun main() {
    val array = arrayOf(1, 2, 3, 4, 5)
    val dropped = array.drop(2)   // removes the first 2 elements
    println(dropped)             // prints: [3, 4, 5]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/drop.html)

    