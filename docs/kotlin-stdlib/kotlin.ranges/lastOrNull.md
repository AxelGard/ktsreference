

# lastOrNull

Returns the last element, or null if the progression is empty.

```kotlin
fun IntProgression.lastOrNull(): Int?(source)
```

```kotlin
fun main() {
    val ascending = 1..5
    println(ascending.lastOrNull())   // prints 5

    val descending = 5 downTo 1
    println(descending.lastOrNull())  // prints 1

    val empty = 5..0
    println(empty.lastOrNull())       // prints null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/last-or-null.html)

    