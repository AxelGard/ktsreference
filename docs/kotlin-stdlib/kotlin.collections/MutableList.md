

# MutableList

Creates a new mutable list with the specified size, where each element is calculated by calling the specified init function.

```kotlin
inline fun <T> MutableList(size: Int, init: (index: Int) -> T): MutableList<T>(source)
```

```kotlin
fun main() {
    val squares = MutableList(5) { index -> index * index }
    println(squares) // [0, 1, 4, 9, 16]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-list.html)

    