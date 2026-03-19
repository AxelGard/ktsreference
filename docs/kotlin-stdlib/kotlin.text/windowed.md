

# windowed

Returns a list of snapshots of the window of the given size sliding along this char sequence with the given step, where each snapshot is a string.

```kotlin
fun CharSequence.windowed(size: Int, step: Int = 1, partialWindows: Boolean = false): List<String>(source)
```

```kotlin
fun main() {
    val text = "123456789"
    // Take windows of size 3, move 2 characters each step, include the last partial window
    val windows = text.windowed(size = 3, step = 2, partialWindows = true)
    println(windows) // [123, 345, 567, 789]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/windowed.html)

    