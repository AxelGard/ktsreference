

# unzip

Returns a pair of lists, where first list is built from the first values of each pair from this sequence, second list is built from the second values of each pair from this sequence.

```kotlin
fun <T, R> Sequence<Pair<T, R>>.unzip(): Pair<List<T>, List<R>>(source)
```

```kotlin
val pairs = listOf(
    Pair("Alice", 28),
    Pair("Bob", 34),
    Pair("Carol", 22)
).asSequence()

val (names, ages) = pairs.unzip()

println(names) // [Alice, Bob, Carol]
println(ages)  // [28, 34, 22]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/unzip.html)

    