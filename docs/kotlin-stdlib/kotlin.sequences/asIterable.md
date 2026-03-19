

# asIterable

Creates an Iterable instance that wraps the original sequence returning its elements when being iterated.

```kotlin
fun <T> Sequence<T>.asIterable(): Iterable<T>(source)
```

```kotlin
import kotlin.sequences.*

fun main() {
    // Create a sequence of the first 5 natural numbers
    val seq = generateSequence(1) { it + 1 }.take(5)

    // Convert the sequence to an Iterable
    val iterable: Iterable<Int> = seq.asIterable()

    // Iterate over the Iterable
    for (number in iterable) {
        println(number)  // prints 1, 2, 3, 4, 5
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/as-iterable.html)

    