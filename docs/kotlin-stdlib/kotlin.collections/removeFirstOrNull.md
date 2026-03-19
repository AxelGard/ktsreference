

# removeFirstOrNull

Removes the first element from this mutable list and returns that removed element, or returns null if this list is empty.

```kotlin
@IgnorableReturnValuefun <T> MutableList<T>.removeFirstOrNull(): T?(source)
```

```kotlin
fun main() {
    val fruits = mutableListOf("apple", "banana", "cherry")
    val firstFruit = fruits.removeFirstOrNull()
    println(firstFruit)   // apple
    println(fruits)       // [banana, cherry]

    val emptyList = mutableListOf<Int>()
    val removed = emptyList.removeFirstOrNull()
    println(removed)      // null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/remove-first-or-null.html)

    