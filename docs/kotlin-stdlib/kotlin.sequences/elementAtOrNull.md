

# elementAtOrNull

Returns an element at the given index or null if the index is out of bounds of this sequence.

```kotlin
fun <T> Sequence<T>.elementAtOrNull(index: Int): T?(source)
```

```kotlin
val numbers = sequenceOf(10, 20, 30, 40)

println(numbers.elementAtOrNull(2))   // Prints: 30
println(numbers.elementAtOrNull(5))   // Prints: null
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/element-at-or-null.html)

    