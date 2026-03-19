

# flatMapIndexedTo

Appends all elements yielded from results of transform function being invoked on each element and its index in the original array, to the given destination.

```kotlin
@JvmName(name = "flatMapIndexedIterableTo")@IgnorableReturnValueinline fun <T, R, C : MutableCollection<in R>> Array<out T>.flatMapIndexedTo(destination: C, transform: (index: Int, T) -> Iterable<R>): C(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3)

val result = mutableListOf<Int>()
numbers.flatMapIndexedTo(result) { index, value ->
    // For each element we produce a list containing its index, the value itself,
    // and the product of the index and the value.
    listOf(index, value, index * value)
}

println(result)   // Output: [0, 1, 0, 1, 2, 4, 2, 3, 6]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/flat-map-indexed-to.html)

    