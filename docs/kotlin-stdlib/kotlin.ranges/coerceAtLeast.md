

# coerceAtLeast

Ensures that this value is not less than the specified minimumValue.

```kotlin
fun <T : Comparable<T>> T.coerceAtLeast(minimumValue: T): T(source)
```

```kotlin
fun main() {
    val currentValue = 5
    val minValue = 10

    val coerced = currentValue.coerceAtLeast(minValue)

    println("Original: $currentValue")
    println("Minimum allowed: $minValue")
    println("Coerced result: $coerced") // prints 10
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/coerce-at-least.html)

    