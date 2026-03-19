

# filterNotTo

Appends all elements not matching the given predicate to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, C : MutableCollection<in T>> Sequence<T>.filterNotTo(destination: C, predicate: (T) -> Boolean): C(source)
```

```kotlin
val numbers = listOf(1, 2, 3, 4, 5)
val result = mutableListOf<Int>()

numbers.asSequence()
    .filterNotTo(result) { it % 2 == 0 }

println(result) // prints: [1, 3, 5]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/filter-not-to.html)

    