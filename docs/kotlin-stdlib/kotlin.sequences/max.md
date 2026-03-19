

# max

Returns the largest element.

```kotlin
@JvmName(name = "maxOrThrow")fun Sequence<Double>.max(): Double(source)
```

```kotlin
fun main() {
    val numbers: Sequence<Double> = listOf(3.5, 1.2, 4.8, 2.9).asSequence()
    val maxValue = numbers.max()   // calls Sequence<Double>.max()
    println("Maximum value: $maxValue")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/max.html)

    