

# zipWithNext

Returns a sequence of pairs of each two adjacent elements in this sequence.

```kotlin
fun <T> Sequence<T>.zipWithNext(): Sequence<Pair<T, T>>(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4)

val pairs = numbers.zipWithNext()

pairs.forEach { (first, second) ->
    println("$first, $second")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/zip-with-next.html)

    