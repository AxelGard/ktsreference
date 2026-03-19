

# nextDown

Returns the Double value nearest to this value in direction of negative infinity.

```kotlin
expect fun Double.nextDown(): Double(source)
```

```kotlin
fun main() {
    val original = 1.0
    val lower = original.nextDown()

    println("Original: $original")
    println("Next down: $lower")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/next-down.html)

    