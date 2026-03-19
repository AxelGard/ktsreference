

# iterator

Builds an Iterator lazily yielding values one by one.

```kotlin
fun <T> iterator(block: suspend SequenceScope<T>.() -> Unit): Iterator<T>(source)
```

```kotlin
import kotlin.sequences.iterator

fun main() {
    val numbers = iterator<Int> {
        for (i in 1..5) {
            yield(i)          // produce the next value lazily
        }
    }

    numbers.forEach { println(it) }   // prints 1 2 3 4 5
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/iterator.html)

    