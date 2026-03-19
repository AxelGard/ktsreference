

# distinct

Returns a sequence containing only distinct elements from the given sequence.

```kotlin
fun <T> Sequence<T>.distinct(): Sequence<T>(source)
```

fun main() {
    val numbers = sequenceOf(1, 2, 2, 3, 4, 4, 5)
    val distinctNumbers = numbers.distinct()
    distinctNumbers.forEach { println(it) }
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/distinct.html)

    