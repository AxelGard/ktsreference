

# minOrNull

Returns the smallest element or null if the sequence is empty.

```kotlin
fun Sequence<Double>.minOrNull(): Double?(source)
```

```kotlin
val numbers = sequenceOf(3.5, 1.2, 4.8, 2.7)
val minValue = numbers.minOrNull()
println("Minimum value: ${minValue ?: "No elements"}")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/min-or-null.html)

    