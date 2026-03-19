

# slice

Returns a list containing elements at indices in the specified indices range.

```kotlin
fun <T> Array<out T>.slice(indices: IntRange): List<T>(source)
```

```kotlin
fun main() {
    val arr = arrayOf("a", "b", "c", "d", "e")
    val selected = arr.slice(2..4)   // takes elements at indices 2, 3, 4
    println(selected)                // Output: [c, d, e]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/slice.html)

    