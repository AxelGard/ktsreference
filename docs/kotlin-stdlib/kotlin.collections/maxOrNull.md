

# maxOrNull

Returns the largest element or null if the array is empty.

```kotlin
fun Array<out Double>.maxOrNull(): Double?(source)
```

```kotlin
val numbers = arrayOf(3.5, 7.2, 1.9, 9.4)

val maxValue: Double? = numbers.maxOrNull()

println(maxValue ?: "Array is empty")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/max-or-null.html)

    