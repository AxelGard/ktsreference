

# filterIndexedTo

Appends all elements matching the given predicate to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, C : MutableCollection<in T>> Sequence<T>.filterIndexedTo(destination: C, predicate: (index: Int, T) -> Boolean): C(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(10, 20, 30, 40, 50)
    val result = mutableListOf<Int>()

    numbers.filterIndexedTo(result) { index, value ->
        index % 2 == 0  // keep elements at even indices
    }

    println(result) // [10, 30, 50]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/filter-indexed-to.html)

    