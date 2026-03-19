

# flatMapTo

Appends all elements yielded from results of transform function being invoked on each element of original sequence, to the given destination.

```kotlin
@JvmName(name = "flatMapIterableTo")@IgnorableReturnValueinline fun <T, R, C : MutableCollection<in R>> Sequence<T>.flatMapTo(destination: C, transform: (T) -> Iterable<R>): C(source)
```

```kotlin
fun main() {
    val seq = sequenceOf(1, 2, 3)
    val destination = mutableListOf<Int>()

    seq.flatMapTo(destination) { n ->
        listOf(n, n * 10)
    }

    println(destination) // [1, 10, 2, 20, 3, 30]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/flat-map-to.html)

    