

# filterTo

Appends all elements matching the given predicate to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, C : MutableCollection<in T>> Sequence<T>.filterTo(destination: C, predicate: (T) -> Boolean): C(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4, 5)
val evens = mutableListOf<Int>()
numbers.filterTo(evens) { it % 2 == 0 }
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/filter-to.html)

    