

# mapIndexedNotNullTo

Applies the given transform function to each element and its index in the original array and appends only the non-null results to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, R : Any, C : MutableCollection<in R>> Array<out T>.mapIndexedNotNullTo(destination: C, transform: (index: Int, T) -> R?): C(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4, 5)

val evenDescriptions = mutableListOf<String>()
numbers.mapIndexedNotNullTo(evenDescriptions) { index, value ->
    if (value % 2 == 0) "Index $index contains even number $value" else null
}

println(evenDescriptions)   // Prints: [Index 1 contains even number 2, Index 3 contains even number 4]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-indexed-not-null-to.html)

    