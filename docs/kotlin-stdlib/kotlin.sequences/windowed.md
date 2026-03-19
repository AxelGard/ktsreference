

# windowed

Returns a sequence of snapshots of the window of the given size sliding along this sequence with the given step, where each snapshot is a list.

```kotlin
fun <T> Sequence<T>.windowed(size: Int, step: Int = 1, partialWindows: Boolean = false): Sequence<List<T>>(source)
```

```kotlin
fun main() {
    val seq = (1..10).asSequence()

    // Create windows of size 3, moving 2 steps at a time, include partial windows
    val windows = seq.windowed(size = 3, step = 2, partialWindows = true)

    windows.forEach { println(it) }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/windowed.html)

    