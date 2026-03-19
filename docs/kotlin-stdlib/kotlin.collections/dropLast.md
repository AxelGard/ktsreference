

# dropLast

Returns a list containing all elements except last n elements.

```kotlin
fun <T> Array<out T>.dropLast(n: Int): List<T>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3, 4, 5)
    val trimmed = numbers.dropLast(2)
    println(trimmed) // [1, 2, 3]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/drop-last.html)

    