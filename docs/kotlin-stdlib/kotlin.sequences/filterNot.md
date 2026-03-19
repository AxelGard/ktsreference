

# filterNot

Returns a sequence containing all elements not matching the given predicate.

```kotlin
fun <T> Sequence<T>.filterNot(predicate: (T) -> Boolean): Sequence<T>(source)
```

```kotlin
val numbers = listOf(1, 2, 3, 4, 5)

val oddNumbers = numbers.asSequence()
    .filterNot { it % 2 == 0 }
    .toList()

println(oddNumbers)   // [1, 3, 5]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/filter-not.html)

    