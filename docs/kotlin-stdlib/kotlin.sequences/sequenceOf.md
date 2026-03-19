

# sequenceOf

Creates a sequence that returns the specified values.

```kotlin
fun <T> sequenceOf(vararg elements: T): Sequence<T>(source)(source)
```

```kotlin
val seq = sequenceOf("apple", "banana", "cherry")

seq.forEach { println(it) }
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/sequence-of.html)

    