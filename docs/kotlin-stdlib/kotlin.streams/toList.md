

# toList

Returns a List containing all elements produced by this stream.

```kotlin
fun <T> Stream<T>.toList(): List<T>(source)
```

```kotlin
import java.util.stream.Stream
import kotlin.streams.toList

fun main() {
    val numbers = Stream.of(10, 20, 30)
    val list: List<Int> = numbers.toList()
    println(list)  // prints [10, 20, 30]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.streams/to-list.html)

    