

# flatMapIndexedTo

Appends all elements yielded from results of transform function being invoked on each element and its index in the original sequence, to the given destination.

```kotlin
@JvmName(name = "flatMapIndexedIterableTo")@IgnorableReturnValueinline fun <T, R, C : MutableCollection<in R>> Sequence<T>.flatMapIndexedTo(destination: C, transform: (index: Int, T) -> Iterable<R>): C(source)
```

```kotlin
val numbers = sequenceOf(10, 20, 30)
val words = mutableListOf<String>()

numbers.flatMapIndexedTo(words) { index, number ->
    listOf(
        "item${index + 1}: $number",
        "double${index + 1}: ${number * 2}"
    )
}

println(words)   // [item1: 10, double1: 20, item2: 20, double2: 40, item3: 30, double3: 60]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/flat-map-indexed-to.html)

    