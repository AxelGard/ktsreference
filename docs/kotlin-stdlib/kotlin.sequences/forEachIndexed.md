

# forEachIndexed

Performs the given action on each element, providing sequential index with the element.

```kotlin
inline fun <T> Sequence<T>.forEachIndexed(action: (index: Int, T) -> Unit)(source)
```

```kotlin
val sequence = sequenceOf("apple", "banana", "cherry")

sequence.forEachIndexed { index, fruit ->
    println("Index $index contains $fruit")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/for-each-indexed.html)

    