

# rangeTo

Creates a range from this Comparable value to the specified that value.

```kotlin
operator fun <T : Comparable<T>> T.rangeTo(that: T): ClosedRange<T>(source)
```

```kotlin
fun main() {
    val range = 1.rangeTo(10)   // creates a ClosedRange<Int> from 1 to 10
    for (i in range) {
        println(i)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/range-to.html)

    