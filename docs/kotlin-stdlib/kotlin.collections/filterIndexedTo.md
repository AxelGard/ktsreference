

# filterIndexedTo

Appends all elements matching the given predicate to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, C : MutableCollection<in T>> Array<out T>.filterIndexedTo(destination: C, predicate: (index: Int, T) -> Boolean): C(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(10, 20, 30, 40, 50)
    val evens = mutableListOf<Int>()

    numbers.filterIndexedTo(evens) { index, value ->
        index % 2 == 0   // keep elements at even indices
    }

    println(evens) // Output: [10, 30, 50]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter-indexed-to.html)

    