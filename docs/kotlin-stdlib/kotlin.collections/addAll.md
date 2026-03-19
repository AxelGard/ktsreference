

# addAll

Adds all elements of the given elements collection to this MutableCollection.

```kotlin
@IgnorableReturnValuefun <T> MutableCollection<in T>.addAll(elements: Iterable<T>): Boolean(source)
```

```kotlin
val numbers = mutableListOf(1, 2, 3)
val moreNumbers = listOf(4, 5, 6)

// add all elements from `moreNumbers` to `numbers`
numbers.addAll(moreNumbers)

// `numbers` now contains: [1, 2, 3, 4, 5, 6]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/add-all.html)

    