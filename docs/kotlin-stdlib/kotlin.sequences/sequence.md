

# sequence

Builds a Sequence lazily yielding values one by one.

```kotlin
fun <T> sequence(block: suspend SequenceScope<T>.() -> Unit): Sequence<T>(source)
```

```kotlin
import kotlin.sequences.*

fun main() {
    val numbers = sequence {
        // Lazy generation of numbers 1..10
        for (i in 1..10) {
            yield(i)
        }
    }

    // Consume the sequence (the values are generated only when needed)
    val sum = numbers.sum()
    println("Sum of 1..10 is $sum")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/sequence.html)

    