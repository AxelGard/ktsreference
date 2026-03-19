

# coerceAtMost

Ensures that this value is not greater than the specified maximumValue.

```kotlin
fun <T : Comparable<T>> T.coerceAtMost(maximumValue: T): T(source)
```

```kotlin
val value = 15
val maximum = 10

val result = value.coerceAtMost(maximum)  // result = 10
println(result)                           // prints: 10
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/coerce-at-most.html)

    