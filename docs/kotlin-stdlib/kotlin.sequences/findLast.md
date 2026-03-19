

# findLast

Returns the last element matching the given predicate, or null if no such element was found.

```kotlin
inline fun <T> Sequence<T>.findLast(predicate: (T) -> Boolean): T?(source)
```

```kotlin
fun main() {
    val numbers = (1..10).asSequence()
    val lastOdd = numbers.findLast { it % 2 != 0 }
    println(lastOdd) // prints 9
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/find-last.html)

    