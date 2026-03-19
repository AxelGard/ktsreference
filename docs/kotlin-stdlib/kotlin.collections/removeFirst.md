

# removeFirst

Removes the first element from this mutable list and returns that removed element, or throws NoSuchElementException if this list is empty.

```kotlin
@IgnorableReturnValuefun <T> MutableList<T>.removeFirst(): T(source)
```

```kotlin
fun main() {
    val numbers = mutableListOf(1, 2, 3)
    val first = numbers.removeFirst()
    println("Removed: $first")          // 1
    println("Remaining list: $numbers") // [2, 3]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/remove-first.html)

    