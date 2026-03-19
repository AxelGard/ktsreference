

# onEachIndexed

Returns a sequence which performs the given action on each element of the original sequence as they pass through it.

```kotlin
fun <T> Sequence<T>.onEachIndexed(action: (index: Int, T) -> Unit): Sequence<T>(source)
```

```kotlin
val numbers = sequenceOf(10, 20, 30, 40, 50)

val list = numbers
    .onEachIndexed { index, value ->
        println("Element at index $index is $value")
    }
    .toList()   // materialize the sequence
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/on-each-indexed.html)

    