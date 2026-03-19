

# asStream

Creates a sequential Stream instance that produces elements from the original sequence.

```kotlin
fun <T> Sequence<T>.asStream(): Stream<T>(source)
```

```kotlin
import kotlin.streams.asStream
import java.util.stream.Collectors

fun main() {
    val numbers = sequenceOf(1, 2, 3, 4, 5, 6)

    val doubledEvens = numbers.asStream()
        .filter { it % 2 == 0 }      // keep only even numbers
        .map { it * 2 }              // double each remaining number
        .collect(Collectors.toList()) // collect into a List

    println(doubledEvens)   // prints: [4, 8, 12]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.streams/as-stream.html)

    