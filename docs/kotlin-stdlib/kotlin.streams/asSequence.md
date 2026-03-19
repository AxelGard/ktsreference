

# asSequence

Creates a Sequence instance that wraps the original stream iterating through its elements.

```kotlin
fun <T> Stream<T>.asSequence(): Sequence<T>(source)
```

```kotlin
import java.util.stream.Stream
import kotlin.streams.asSequence

fun main() {
    val stream: Stream<Int> = Stream.of(1, 2, 3, 4, 5)

    val result = stream.asSequence()
        .filter { it % 2 == 0 }   // keep only even numbers
        .map { it * 10 }          // multiply each by 10
        .toList()                 // collect into a List

    println(result)  // prints: [20, 40]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.streams/as-sequence.html)

    