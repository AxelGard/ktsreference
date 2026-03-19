

# removeLastOrNull

Removes the last element from this mutable list and returns that removed element, or returns null if this list is empty.

```kotlin
@IgnorableReturnValuefun <T> MutableList<T>.removeLastOrNull(): T?(source)
```

```kotlin
fun main() {
    val list = mutableListOf("one", "two", "three")
    val last = list.removeLastOrNull()
    println("Removed: $last")
    println("List now: $list")

    val empty = mutableListOf<Int>()
    val result = empty.removeLastOrNull()
    println("Result from empty list: $result")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/remove-last-or-null.html)

    