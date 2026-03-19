

# windowedSequence

Returns a sequence of snapshots of the window of the given size sliding along this char sequence with the given step, where each snapshot is a string.

```kotlin
fun CharSequence.windowedSequence(size: Int, step: Int = 1, partialWindows: Boolean = false): Sequence<String>(source)
```

```kotlin
val text = "abcdefg"
val windows = text.windowedSequence(size = 3, step = 2, partialWindows = true).toList()
println(windows) // Output: [abc, cde, efg]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/windowed-sequence.html)

    