

# min

Returns the smallest element.

```kotlin
@JvmName(name = "minOrThrow")fun Sequence<Double>.min(): Double(source)
```

```kotlin
fun main() {
    val numbers = listOf(10.5, 3.2, 7.8, 1.9).asSequence()
    val minValue = numbers.min()
    println("Minimum value is $minValue")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/min.html)

    