

# firstOrNull

Returns the first element, or null if the progression is empty.

```kotlin
fun IntProgression.firstOrNull(): Int?(source)
```

```kotlin
fun main() {
    val nonEmpty = 1..5
    println(nonEmpty.firstOrNull()) // Prints: 1

    val empty = 5..1  // IntRange that yields no values
    println(empty.firstOrNull())  // Prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/first-or-null.html)

    