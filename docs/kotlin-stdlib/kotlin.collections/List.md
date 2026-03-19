

# List

Creates a new read-only list with the specified size, where each element is calculated by calling the specified init function.

```kotlin
inline fun <T> List(size: Int, init: (index: Int) -> T): List<T>(source)
```

```kotlin
fun main() {
    val squares = List(5) { index -> index * index }
    println(squares) // Output: [0, 1, 4, 9, 16]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list.html)

    