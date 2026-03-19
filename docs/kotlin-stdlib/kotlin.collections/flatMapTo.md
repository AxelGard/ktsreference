

# flatMapTo

Appends all elements yielded from results of transform function being invoked on each element of original array, to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, R, C : MutableCollection<in R>> Array<out T>.flatMapTo(destination: C, transform: (T) -> Iterable<R>): C(source)
```

```kotlin
val numbersByGroup = arrayOf(
    listOf(1, 2, 3),
    listOf(4, 5),
    listOf(6)
)

val flattened = mutableListOf<Int>()
numbersByGroup.flatMapTo(flattened) { it }

println(flattened)   // Output: [1, 2, 3, 4, 5, 6]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/flat-map-to.html)

    