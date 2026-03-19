

# windowed

Returns a list of snapshots of the window of the given size sliding along this collection with the given step, where each snapshot is a list.

```kotlin
fun <T> Iterable<T>.windowed(size: Int, step: Int = 1, partialWindows: Boolean = false): List<List<T>>(source)
```

```kotlin
fun main() {
    val list = listOf(1, 2, 3, 4, 5, 6)
    val windows = list.windowed(size = 3, step = 2, partialWindows = true)
    println(windows)   // Output: [[1, 2, 3], [3, 4, 5], [5, 6]]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/windowed.html)

    