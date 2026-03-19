

# mapNotNullTo

Applies the given transform function to each element in the original sequence and appends only the non-null results to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, R : Any, C : MutableCollection<in R>> Sequence<T>.mapNotNullTo(destination: C, transform: (T) -> R?): C(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4, 5)

val evenDescriptions = mutableListOf<String>()
numbers.mapNotNullTo(evenDescriptions) { n ->
    if (n % 2 == 0) "Number $n" else null
}

println(evenDescriptions) // [Number 2, Number 4]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/map-not-null-to.html)

    