

# minOrNull

Returns the smallest element or null if the array is empty.

```kotlin
fun Array<out Double>.minOrNull(): Double?(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(3.5, 1.2, 4.8, 0.9)
    val minValue = numbers.minOrNull()
    println("Smallest number: $minValue")  // Output: Smallest number: 0.9
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/min-or-null.html)

    