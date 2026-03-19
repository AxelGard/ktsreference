

# contains

Returns true if element is found in the sequence.

```kotlin
operator fun <T> Sequence<T>.contains(element: T): Boolean(source)
```

```kotlin
val seq = listOf(10, 20, 30, 40, 50).asSequence()

println(30 in seq)      // true
println(25 in seq)      // false
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/contains.html)

    