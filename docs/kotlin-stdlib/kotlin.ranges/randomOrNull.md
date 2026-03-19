

# randomOrNull

Returns a random element from this range, or null if this range is empty.

```kotlin
inline fun IntRange.randomOrNull(): Int?(source)
```

```kotlin
fun main() {
    val range = 1..10
    val randomValue = range.randomOrNull()
    println("Random value from 1..10: $randomValue")

    val emptyRange = 5..4
    val nullValue = emptyRange.randomOrNull()
    println("Random value from empty range: $nullValue") // null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/random-or-null.html)

    