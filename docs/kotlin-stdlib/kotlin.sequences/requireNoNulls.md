

# requireNoNulls

Returns an original collection containing all the non-null elements, throwing an IllegalArgumentException if there are any null elements.

```kotlin
fun <T : Any> Sequence<T?>.requireNoNulls(): Sequence<T>(source)
```

```kotlin
val nullableInts = listOf(1, null, 3)
val nonNullInts: List<Int> = nullableInts
    .asSequence()
    .requireNoNulls()
    .toList()   // throws IllegalArgumentException because of the null
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/require-no-nulls.html)

    