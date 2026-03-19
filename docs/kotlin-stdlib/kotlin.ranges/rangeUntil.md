

# rangeUntil

Creates an open-ended range from this Comparable value to the specified that value.

```kotlin
operator fun <T : Comparable<T>> T.rangeUntil(that: T): OpenEndRange<T>(source)
```

```kotlin
val openRange = 1.rangeUntil(5)   // 1..5 (exclusive of 5)

for (value in openRange) {
    println(value)   // prints 1, 2, 3, 4
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/range-until.html)

    