

# ifEmpty

Returns a sequence that iterates through the elements either of this sequence or, if this sequence turns out to be empty, of the sequence returned by defaultValue function.

```kotlin
fun <T> Sequence<T>.ifEmpty(defaultValue: () -> Sequence<T>): Sequence<T>(source)
```

```kotlin
val emptySeq = emptySequence<Int>()          // an empty sequence
val defaultSeq = sequenceOf(1, 2, 3)          // fallback values

val result = emptySeq.ifEmpty { defaultSeq }

println(result.toList())   // prints: [1, 2, 3]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/if-empty.html)

    