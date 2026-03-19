

# filterIsInstance

Returns a sequence containing all elements that are instances of specified type parameter R.

```kotlin
inline fun <R> Sequence<*>.filterIsInstance(): Sequence<R>(source)
```

```kotlin
val mixedSequence = sequenceOf(1, "two", 3, "four", 5)
val intSequence: Sequence<Int> = mixedSequence.filterIsInstance()
val ints = intSequence.toList()          // [1, 3, 5]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/filter-is-instance.html)

    