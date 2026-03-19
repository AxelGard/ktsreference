

# removeLast

Removes the last element from this mutable list and returns that removed element, or throws NoSuchElementException if this list is empty.

```kotlin
@IgnorableReturnValuefun <T> MutableList<T>.removeLast(): T(source)
```

```kotlin
fun main() {
    val fruits = mutableListOf("apple", "banana", "cherry")
    val removed = fruits.removeLast()
    println("Removed element: $removed")  // cherry
    println("List after removal: $fruits") // [apple, banana]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/remove-last.html)

    