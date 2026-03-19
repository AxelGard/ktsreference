

# indexOfLast

Returns index of the last element matching the given predicate, or -1 if the sequence does not contain such element.

```kotlin
inline fun <T> Sequence<T>.indexOfLast(predicate: (T) -> Boolean): Int(source)
```

```kotlin
fun main() {
    val fruits = sequenceOf("apple", "banana", "cherry", "date", "fig")

    // Find the last index of an element that contains the letter 'a'
    val lastIndexWithA = fruits.indexOfLast { it.contains('a') } // 3 ("date")
    println(lastIndexWithA)

    // Find the last index of an element that contains the letter 'z' (none)
    val lastIndexWithZ = fruits.indexOfLast { it.contains('z') } // -1
    println(lastIndexWithZ)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/index-of-last.html)

    