

# zip

Returns a sequence of values built from the elements of this sequence and the other sequence with the same index. The resulting sequence ends as soon as the shortest input sequence ends.

```kotlin
infix fun <T, R> Sequence<T>.zip(other: Sequence<R>): Sequence<Pair<T, R>>(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4)
val words   = sequenceOf("one", "two", "three")

val zipped = numbers zip words

zipped.forEach { (num, word) ->
    println("$num -> $word")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/zip.html)

    