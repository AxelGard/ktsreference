

# drop

Returns a sequence containing all elements except first n elements.

```kotlin
fun <T> Sequence<T>.drop(n: Int): Sequence<T>(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4, 5)
val dropped = numbers.drop(2)

println(dropped.toList()) // Output: [3, 4, 5]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/drop.html)

    