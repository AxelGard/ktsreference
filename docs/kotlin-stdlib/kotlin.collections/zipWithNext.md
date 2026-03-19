

# zipWithNext

Returns a list of pairs of each two adjacent elements in this collection.

```kotlin
fun <T> Iterable<T>.zipWithNext(): List<Pair<T, T>>(source)
```

```kotlin
val numbers = listOf(10, 20, 30, 40, 50)
val adjacentPairs = numbers.zipWithNext()   // [(10, 20), (20, 30), (30, 40), (40, 50)]

println(adjacentPairs)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/zip-with-next.html)

    