

# coerceIn

Ensures that this value lies in the specified range minimumValue..maximumValue.

```kotlin
fun <T : Comparable<T>> T.coerceIn(minimumValue: T?, maximumValue: T?): T(source)
```

```kotlin
val value = 120
val clamped = value.coerceIn(0, 100)
println(clamped)  // Output: 100
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/coerce-in.html)

    