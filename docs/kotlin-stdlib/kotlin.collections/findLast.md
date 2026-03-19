

# findLast

Returns the last element matching the given predicate, or null if no such element was found.

```kotlin
inline fun <T> Array<out T>.findLast(predicate: (T) -> Boolean): T?(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 3, 5, 7, 9)

    val lastEven = numbers.findLast { it % 2 == 0 }   // null
    val lastOdd  = numbers.findLast { it % 2 != 0 }   // 9

    println("Last even number: $lastEven")
    println("Last odd number: $lastOdd")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/find-last.html)

    