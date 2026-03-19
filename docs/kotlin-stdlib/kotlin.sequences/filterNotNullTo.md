

# filterNotNullTo

Appends all elements that are not null to the given destination.

```kotlin
@IgnorableReturnValuefun <C : MutableCollection<in T>, T : Any> Sequence<T?>.filterNotNullTo(destination: C): C(source)
```

```kotlin
val nullableNumbers: Sequence<Int?> = sequenceOf(1, null, 2, null, 3)
val nonNullList = mutableListOf<Int>()

nullableNumbers.filterNotNullTo(nonNullList)

// nonNullList now contains [1, 2, 3]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/filter-not-null-to.html)

    