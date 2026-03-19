

# elementAt

Returns an element at the given index or throws an IndexOutOfBoundsException if the index is out of bounds of this collection.

```kotlin
fun <T> Iterable<T>.elementAt(index: Int): T(source)
```

```kotlin
val fruits = listOf("apple", "banana", "cherry")
val secondFruit = fruits.elementAt(1)   // "banana"
println(secondFruit)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/element-at.html)

    