

# indexOfFirst

Returns index of the first element matching the given predicate, or -1 if the sequence does not contain such element.

```kotlin
inline fun <T> Sequence<T>.indexOfFirst(predicate: (T) -> Boolean): Int(source)
```

```kotlin
fun main() {
    val fruits = sequenceOf("apple", "banana", "cherry", "date")

    // Find the index of the first fruit that starts with 'c'
    val index = fruits.indexOfFirst { it.startsWith('c') }

    println(index)   // Output: 2
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/index-of-first.html)

    